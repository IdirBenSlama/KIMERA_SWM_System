#!/usr/bin/env python3
"""
Migrate data from SQLite to PostgreSQL for Kimera SWM
"""

import os
import sys
from datetime import datetime
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import json
from tqdm import tqdm

# Initialize structured logger
from backend.utils.kimera_logger import get_system_logger
logger = get_system_logger(__name__)


# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.vault.database import Base, GeoidDB, ScarDB
from backend.vault.enhanced_database_schema import (
    MultimodalGroundingDB, CausalRelationshipDB, SelfModelDB,
    IntrospectionLogDB, CompositionSemanticDB, ConceptualAbstractionDB,
    ValueSystemDB, GenuineOpinionDB, EthicalReasoningDB,
    EnhancedScarDB, EnhancedGeoidDB, UnderstandingTestDB,
    ConsciousnessIndicatorDB
)

def migrate_data():
    """Migrate all data from SQLite to PostgreSQL"""
    
    logger.info("🚀 Kimera SWM SQLite to PostgreSQL Migration")
    logger.info("=" * 50)
    
    # Database URLs
    sqlite_url = os.getenv("SQLITE_DATABASE_URL", "sqlite:///./kimera_swm.db")
    postgres_url = os.getenv("DATABASE_URL", "postgresql://kimera:kimera_secure_pass_2025@localhost:5432/kimera_swm")
    
    if "postgresql" not in postgres_url:
        logger.error("❌ DATABASE_URL must be a PostgreSQL URL")
        return False
    
    logger.info(f"📂 Source: {sqlite_url}")
    logger.info(f"📂 Target: {postgres_url}")
    
    try:
        # Create engines
        sqlite_engine = create_engine(sqlite_url)
        postgres_engine = create_engine(postgres_url)
        
        # Test connections
        with sqlite_engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            logger.info("✅ SQLite connection successful")
        
        with postgres_engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            logger.info("✅ PostgreSQL connection successful")
        
        # Create all tables in PostgreSQL
        logger.info("\n📊 Creating PostgreSQL schema...")
        Base.metadata.create_all(postgres_engine)
        logger.info("✅ Schema created")
        
        # Create sessions
        SqliteSession = sessionmaker(bind=sqlite_engine)
        PostgresSession = sessionmaker(bind=postgres_engine)
        
        sqlite_session = SqliteSession()
        postgres_session = PostgresSession()
        
        # Tables to migrate in order (respecting foreign keys)
        tables = [
            (GeoidDB, "Geoids"),
            (ScarDB, "SCARs"),
            (MultimodalGroundingDB, "Multimodal Groundings"),
            (CausalRelationshipDB, "Causal Relationships"),
            (SelfModelDB, "Self Models"),
            (IntrospectionLogDB, "Introspection Logs"),
            (CompositionSemanticDB, "Compositional Semantics"),
            (ConceptualAbstractionDB, "Conceptual Abstractions"),
            (ValueSystemDB, "Value Systems"),
            (GenuineOpinionDB, "Genuine Opinions"),
            (EthicalReasoningDB, "Ethical Reasoning"),
            (EnhancedScarDB, "Enhanced SCARs"),
            (EnhancedGeoidDB, "Enhanced Geoids"),
            (UnderstandingTestDB, "Understanding Tests"),
            (ConsciousnessIndicatorDB, "Consciousness Indicators")
        ]
        
        logger.info("\n🔄 Starting data migration...")
        total_migrated = 0
        
        for table_class, table_name in tables:
            logger.info(f"\n📋 Migrating {table_name}...")
            
            try:
                # Get all records from SQLite
                records = sqlite_session.query(table_class).all()
                count = len(records)
                
                if count == 0:
                    logger.info(f"   No records to migrate")
                    continue
                
                # Migrate records with progress bar
                with tqdm(total=count, desc=f"   {table_name}") as pbar:
                    for record in records:
                        # Create new instance with all attributes
                        new_record = table_class()
                        
                        # Copy all attributes
                        for column in table_class.__table__.columns:
                            if hasattr(record, column.name):
                                setattr(new_record, column.name, getattr(record, column.name))
                        
                        # Add to PostgreSQL session
                        postgres_session.add(new_record)
                        pbar.update(1)
                
                # Commit this table's data
                postgres_session.commit()
                logger.info(f"   ✅ Migrated {count} records")
                total_migrated += count
                
            except Exception as e:
                logger.error(f"   ❌ Error migrating {table_name}: {e}")
                postgres_session.rollback()
                continue
        
        # Update sequences for PostgreSQL
        logger.debug("\n🔧 Updating PostgreSQL sequences...")
        with postgres_engine.connect() as conn:
            # Get all sequences and update them
            sequences = conn.execute(text("""
                SELECT sequence_name, 
                       REPLACE(sequence_name, '_id_seq', '') as table_name
                FROM information_schema.sequences 
                WHERE sequence_schema = 'public'
            """)).fetchall()
            
            for seq_name, table_name in sequences:
                try:
                    conn.execute(text(f"""
                        SELECT setval('{seq_name}', 
                            COALESCE((SELECT MAX(id) FROM {table_name}), 1)
                        )
                    """))
                    conn.commit()
                except:
                    pass  # Some tables might not have id column
        
        logger.info(f"\n✅ Migration complete! Migrated {total_migrated} total records")
        
        # Verify migration
        logger.debug("\n🔍 Verifying migration...")
        verify_migration(sqlite_session, postgres_session)
        
        # Close sessions
        sqlite_session.close()
        postgres_session.close()
        
        return True
        
    except Exception as e:
        logger.error(f"\n��� Migration failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def verify_migration(sqlite_session, postgres_session):
    """Verify that migration was successful"""
    
    tables_to_check = [
        (GeoidDB, "Geoids"),
        (ScarDB, "SCARs"),
        (MultimodalGroundingDB, "Multimodal Groundings")
    ]
    
    all_match = True
    
    for table_class, table_name in tables_to_check:
        sqlite_count = sqlite_session.query(table_class).count()
        postgres_count = postgres_session.query(table_class).count()
        
        if sqlite_count == postgres_count:
            logger.info(f"   ✅ {table_name}: {postgres_count} records")
        else:
            logger.error(f"   ❌ {table_name}: SQLite={sqlite_count}, PostgreSQL={postgres_count}")
            all_match = False
    
    if all_match:
        logger.info("\n✅ All counts match!")
    else:
        logger.warning("\n⚠️  Some counts don't match - manual verification needed")

def create_indexes():
    """Create performance indexes on PostgreSQL"""
    
    logger.debug("\n🔧 Creating performance indexes...")
    
    postgres_url = os.getenv("DATABASE_URL", "postgresql://kimera:kimera_secure_pass_2025@localhost:5432/kimera_swm")
    engine = create_engine(postgres_url)
    
    indexes = [
        # Vector similarity indexes
        "CREATE INDEX IF NOT EXISTS idx_geoids_semantic_vector ON geoids USING ivfflat (semantic_vector vector_cosine_ops) WITH (lists = 100);",
        "CREATE INDEX IF NOT EXISTS idx_scars_scar_vector ON scars USING ivfflat (scar_vector vector_cosine_ops) WITH (lists = 100);",
        
        # JSON indexes
        "CREATE INDEX IF NOT EXISTS idx_geoids_symbolic_gin ON geoids USING gin (symbolic_state);",
        "CREATE INDEX IF NOT EXISTS idx_geoids_metadata_gin ON geoids USING gin (metadata_json);",
        
        # Timestamp indexes
        "CREATE INDEX IF NOT EXISTS idx_scars_timestamp ON scars (timestamp DESC);",
        "CREATE INDEX IF NOT EXISTS idx_scars_vault_timestamp ON scars (vault_id, timestamp DESC);",
        
        # Foreign key indexes
        "CREATE INDEX IF NOT EXISTS idx_multimodal_concept ON multimodal_groundings (concept_id);",
        "CREATE INDEX IF NOT EXISTS idx_causal_cause ON causal_relationships (cause_concept_id);",
        "CREATE INDEX IF NOT EXISTS idx_causal_effect ON causal_relationships (effect_concept_id);"
    ]
    
    with engine.connect() as conn:
        for index_sql in indexes:
            try:
                conn.execute(text(index_sql))
                conn.commit()
                logger.info(f"   ✅ Created index: {index_sql.split('idx_')
            except Exception as e:
                logger.warning(f"   ⚠️  Index creation failed: {e}")

if __name__ == "__main__":
    # Load environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    logger.info("📝 Note: Make sure PostgreSQL is running and accessible")
    logger.info("   docker-compose up -d postgres")
    logger.info()
    
    response = input("Continue with migration? (y/n): ")
    if response.lower() == 'y':
        if migrate_data():
            create_indexes()
            logger.info("\n🎉 Migration successful!")
            logger.info("\n📝 Next steps:")
            logger.info("1. Update your .env file to use PostgreSQL URL")
            logger.info("2. Restart the Kimera application")
            logger.info("3. Verify everything works correctly")
        else:
            logger.error("\n❌ Migration failed - check errors above")
    else:
        logger.info("Migration cancelled")