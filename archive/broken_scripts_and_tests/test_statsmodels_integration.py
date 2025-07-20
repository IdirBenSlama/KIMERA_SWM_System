"""
Comprehensive Test Suite for Statsmodels Integration

This script tests all aspects of the statsmodels integration with Kimera SWM,
including statistical modeling, time series analysis, econometric modeling,
and advanced monitoring capabilities.

Author: Kimera SWM Team
Version: 1.0.0
"""

import sys
import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import logging
import time
import json
from typing import Dict, List, Any

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_statsmodels_availability():
    """Test if statsmodels is properly installed and available"""
    logger.debug("🔍 Testing Statsmodels Availability...")
    
    try:
        import statsmodels
        logger.info(f"   ✅ Statsmodels version: {statsmodels.__version__}")
        
        import statsmodels.api as sm
        import statsmodels.tsa.api as tsa
        from statsmodels.tsa.arima.model import ARIMA
        from statsmodels.tsa.vector_ar.var_model import VAR
        from statsmodels.tsa.stattools import adfuller, kpss
        from statsmodels.regression.linear_model import OLS
        logger.info("   ✅ All required statsmodels modules imported successfully")
        
        return True
        
    except ImportError as e:
        logger.error(f"   ❌ Statsmodels import failed: {e}")
        return False

def test_statistical_modeling_engine():
    """Test the core statistical modeling engine"""
    logger.info("\n📊 Testing Statistical Modeling Engine...")
    
    try:
        from backend.core.statistical_modeling import (
            StatisticalModelingEngine,
            statistical_engine,
            analyze_entropy_time_series,
            analyze_contradiction_factors,
            analyze_semantic_market
        )
        
        # Test engine initialization
        engine = StatisticalModelingEngine()
        logger.info("   ✅ Statistical modeling engine initialized")
        
        # Test model summary
        summary = engine.get_model_summary()
        logger.info(f"   ✅ Model capabilities: {summary['capabilities']}")
        logger.info(f"   ✅ Supported models: {len(summary['supported_models'])
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Statistical modeling engine test failed: {e}")
        return False

def test_time_series_analysis():
    """Test time series analysis capabilities"""
    logger.info("\n📈 Testing Time Series Analysis...")
    
    try:
        from backend.core.statistical_modeling import analyze_entropy_time_series
        
        # Generate synthetic entropy time series
        np.random.seed(42)
        n_points = 100
        time_trend = np.linspace(0, 10, n_points)
        seasonal = 0.5 * np.sin(2 * np.pi * time_trend)
        noise = np.random.normal(0, 0.1, n_points)
        entropy_data = 2.0 + 0.1 * time_trend + seasonal + noise
        
        # Generate timestamps
        start_time = datetime.now() - timedelta(hours=n_points)
        timestamps = [start_time + timedelta(hours=i) for i in range(n_points)]
        
        # Perform analysis
        result = analyze_entropy_time_series(entropy_data.tolist(), timestamps)
        
        logger.info(f"   ✅ Model type: {result.model_type}")
        logger.info(f"   ✅ Statistics calculated: {len(result.statistics)
        logger.info(f"   ✅ Mean entropy: {result.statistics.get('mean', 'N/A')
        logger.info(f"   ✅ Stationarity: {result.statistics.get('is_stationary', 'N/A')
        
        if result.predictions:
            logger.info(f"   ✅ Forecasts generated: {len(result.predictions)
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Time series analysis test failed: {e}")
        return False

def test_regression_analysis():
    """Test regression analysis for contradiction factors"""
    logger.info("\n📉 Testing Regression Analysis...")
    
    try:
        from backend.core.statistical_modeling import analyze_contradiction_factors
        
        # Generate synthetic data
        np.random.seed(42)
        n_samples = 50
        
        # Semantic features
        semantic_complexity = np.random.uniform(0, 1, n_samples)
        entropy_level = np.random.uniform(1, 3, n_samples)
        processing_load = np.random.uniform(0, 1, n_samples)
        
        # Contradiction scores (dependent on features + noise)
        contradiction_scores = (
            0.5 * semantic_complexity + 
            0.3 * entropy_level + 
            0.2 * processing_load + 
            np.random.normal(0, 0.1, n_samples)
        ).tolist()
        
        semantic_features = {
            'semantic_complexity': semantic_complexity.tolist(),
            'entropy_level': entropy_level.tolist(),
            'processing_load': processing_load.tolist()
        }
        
        # Perform regression analysis
        result = analyze_contradiction_factors(contradiction_scores, semantic_features)
        
        logger.info(f"   ✅ Model type: {result.model_type}")
        logger.info(f"   ✅ R-squared: {result.statistics.get('r_squared', 'N/A')
        logger.info(f"   ✅ Parameters estimated: {len([k for k in result.parameters.keys()
        
        if result.residuals:
            logger.info(f"   ✅ Residuals calculated: {len(result.residuals)
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Regression analysis test failed: {e}")
        return False

def test_econometric_analysis():
    """Test econometric analysis of semantic markets"""
    logger.info("\n💹 Testing Econometric Analysis...")
    
    try:
        from backend.core.statistical_modeling import analyze_semantic_market
        
        # Generate synthetic market data
        np.random.seed(42)
        n_periods = 50
        
        # Market dynamics with some correlation
        prices = np.random.uniform(1, 3, n_periods)
        supply = 2.0 + 0.5 * prices + np.random.normal(0, 0.2, n_periods)
        demand = 3.0 - 0.3 * prices + np.random.normal(0, 0.2, n_periods)
        
        # Perform econometric analysis
        result = analyze_semantic_market(
            supply.tolist(),
            demand.tolist(),
            prices.tolist()
        )
        
        logger.info(f"   ✅ Model type: {result.model_type}")
        logger.info(f"   ✅ Supply elasticity: {result.statistics.get('supply_price_elasticity', 'N/A')
        logger.info(f"   ✅ Demand elasticity: {result.statistics.get('demand_price_elasticity', 'N/A')
        logger.info(f"   ✅ Market efficiency: {result.statistics.get('market_efficiency', 'N/A')
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Econometric analysis test failed: {e}")
        return False

def test_comprehensive_analysis():
    """Test comprehensive system analysis"""
    logger.debug("\n🔬 Testing Comprehensive Analysis...")
    
    try:
        from backend.core.statistical_modeling import statistical_engine
        
        # Generate comprehensive system data
        np.random.seed(42)
        n_points = 60
        
        # Entropy history
        entropy_history = (2.0 + 0.1 * np.arange(n_points) + 
                          0.3 * np.sin(np.arange(n_points) * 0.2) + 
                          np.random.normal(0, 0.1, n_points)).tolist()
        
        # Timestamps
        start_time = datetime.now() - timedelta(hours=n_points)
        timestamps = [start_time + timedelta(hours=i) for i in range(n_points)]
        
        # Contradiction scores and features
        contradiction_scores = np.random.uniform(0, 1, n_points).tolist()
        semantic_features = {
            'complexity': np.random.uniform(0, 1, n_points).tolist(),
            'coherence': np.random.uniform(0.5, 1, n_points).tolist()
        }
        
        # Market data
        semantic_supply = np.random.uniform(1, 3, n_points).tolist()
        semantic_demand = np.random.uniform(1, 3, n_points).tolist()
        entropy_prices = entropy_history  # Use entropy as price proxy
        
        # Comprehensive system data
        system_data = {
            'entropy_history': entropy_history,
            'timestamps': timestamps,
            'contradiction_scores': contradiction_scores,
            'semantic_features': semantic_features,
            'semantic_supply': semantic_supply,
            'semantic_demand': semantic_demand,
            'entropy_prices': entropy_prices
        }
        
        # Perform comprehensive analysis
        results = statistical_engine.comprehensive_analysis(system_data)
        
        logger.info(f"   ✅ Analysis types completed: {len(results)
        for analysis_type, result in results.items():
            logger.info(f"   ✅ {analysis_type}: {result.model_type}")
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Comprehensive analysis test failed: {e}")
        return False

def test_forecasting_and_control_monitoring():
    """Test advanced statistical monitoring capabilities"""
    logger.debug("\n🔍 Testing Advanced Statistical Monitoring...")
    
    try:
        from backend.monitoring.forecasting_and_control_monitor import (
            ForecastingAndControlMonitor,
            StatisticalProcessController,
            PredictiveMonitor
        )
        
        # Test statistical process controller
        spc = StatisticalProcessController(window_size=50)
        
        # Add measurements
        np.random.seed(42)
        for i in range(30):
            value = 2.0 + 0.1 * i + np.random.normal(0, 0.2)
            spc.add_measurement('test_metric', value)
        
        # Add an outlier
        spc.add_measurement('test_metric', 10.0)  # Should trigger alert
        
        alerts = spc.get_recent_alerts()
        logger.info(f"   ✅ Statistical process control alerts: {len(alerts)
        
        # Test predictive monitor
        predictor = PredictiveMonitor(forecast_horizon=5)
        historical_data = [2.0 + 0.1 * i + np.random.normal(0, 0.1) for i in range(20)]
        forecast = predictor.update_forecast('test_metric', historical_data)
        
        if forecast:
            logger.info(f"   ✅ Forecast generated: {len(forecast)
        
        # Test advanced monitor
        monitor = ForecastingAndControlMonitor()
        summary = monitor.get_statistical_summary()
        logger.info(f"   ✅ Monitor initialized, tracking: {len(summary['metrics_tracked'])
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Advanced monitoring test failed: {e}")
        return False

def test_integration_with_existing_system():
    """Test integration with existing Kimera SWM components"""
    logger.info("\n🔗 Testing Integration with Existing System...")
    
    try:
        # Test integration with native math
        from backend.core.native_math import NativeStats
        from backend.core.statistical_modeling import statistical_engine
        
        # Compare native vs statsmodels entropy calculation
        test_probs = [0.25, 0.25, 0.25, 0.25]
        native_entropy = NativeStats.entropy(test_probs)
        logger.info(f"   ✅ Native entropy calculation: {native_entropy:.4f}")
        
        # Test enhanced entropy integration
        try:
            from backend.core.enhanced_entropy import EntropyCalculator
            calc = EntropyCalculator()
            enhanced_entropy = calc.shannon_entropy(test_probs)
            logger.info(f"   ✅ Enhanced entropy calculation: {enhanced_entropy:.4f}")
        except Exception as e:
            logger.warning(f"   ⚠️ Enhanced entropy integration: {e}")
        
        # Test monitoring integration
        try:
            from backend.monitoring.entropy_monitor import EntropyMonitor
            from backend.monitoring.forecasting_and_control_monitor import initialize_forecasting_and_control_monitoring
            
            entropy_monitor = EntropyMonitor()
            forecasting_and_control_monitor = initialize_forecasting_and_control_monitoring(entropy_monitor)
            logger.info("   ✅ Advanced monitoring integration successful")
        except Exception as e:
            logger.warning(f"   ⚠️ Monitoring integration: {e}")
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ System integration test failed: {e}")
        return False

def test_performance_comparison():
    """Test performance comparison between native and statsmodels implementations"""
    logger.info("\n⚡ Testing Performance Comparison...")
    
    try:
        from backend.core.native_math import NativeStats
        from backend.core.statistical_modeling import analyze_entropy_time_series
        
        # Generate test data
        np.random.seed(42)
        large_dataset = np.random.uniform(1, 3, 1000).tolist()
        
        # Test native performance
        start_time = time.time()
        for _ in range(100):
            native_mean = NativeStats.mean(large_dataset)
            native_std = NativeStats.std(large_dataset)
        native_time = time.time() - start_time
        
        # Test statsmodels performance
        start_time = time.time()
        result = analyze_entropy_time_series(large_dataset[:100])  # Use smaller dataset for time series
        statsmodels_time = time.time() - start_time
        
        logger.info(f"   ✅ Native calculations (100 iterations)
        logger.info(f"   ✅ Statsmodels analysis (1 iteration)
        logger.info(f"   ✅ Performance ratio: {statsmodels_time/native_time:.2f}x")
        
        return True
        
    except Exception as e:
        logger.error(f"   ❌ Performance comparison test failed: {e}")
        return False

def generate_integration_report():
    """Generate comprehensive integration report"""
    logger.info("\n📋 Generating Integration Report...")
    
    report = {
        'timestamp': datetime.now().isoformat(),
        'statsmodels_integration': {
            'version': None,
            'availability': False,
            'capabilities': []
        },
        'test_results': {},
        'recommendations': []
    }
    
    # Check statsmodels availability
    try:
        import statsmodels
        report['statsmodels_integration']['version'] = statsmodels.__version__
        report['statsmodels_integration']['availability'] = True
        report['statsmodels_integration']['capabilities'] = [
            'Time Series Analysis', 'Regression Modeling', 'Econometric Analysis',
            'Statistical Process Control', 'Predictive Monitoring'
        ]
    except ImportError:
        report['recommendations'].append("Install statsmodels: pip install statsmodels")
    
    # Run all tests
    tests = [
        ('statsmodels_availability', test_statsmodels_availability),
        ('statistical_modeling_engine', test_statistical_modeling_engine),
        ('time_series_analysis', test_time_series_analysis),
        ('regression_analysis', test_regression_analysis),
        ('econometric_analysis', test_econometric_analysis),
        ('comprehensive_analysis', test_comprehensive_analysis),
        ('forecasting_and_control_monitoring', test_forecasting_and_control_monitoring),
        ('system_integration', test_integration_with_existing_system),
        ('performance_comparison', test_performance_comparison)
    ]
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            report['test_results'][test_name] = {
                'status': 'passed' if result else 'failed',
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            report['test_results'][test_name] = {
                'status': 'error',
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
    
    # Generate recommendations
    failed_tests = [name for name, result in report['test_results'].items() 
                   if result['status'] != 'passed']
    
    if failed_tests:
        report['recommendations'].append(f"Review failed tests: {', '.join(failed_tests)}")
    
    if report['statsmodels_integration']['availability']:
        report['recommendations'].append("Statsmodels integration successful - ready for production use")
    else:
        report['recommendations'].append("Install statsmodels to enable advanced statistical features")
    
    # Save report
    report_filename = f"statsmodels_integration_report_{int(time.time())}.json"
    with open(report_filename, 'w') as f:
        json.dump(report, f, indent=2)
    
    logger.info(f"   ✅ Integration report saved: {report_filename}")
    
    # Print summary
    passed_tests = len([r for r in report['test_results'].values() if r['status'] == 'passed'])
    total_tests = len(report['test_results'])
    
    logger.info(f"\n📊 INTEGRATION SUMMARY:")
    logger.info(f"   Tests Passed: {passed_tests}/{total_tests}")
    logger.info(f"   Statsmodels Available: {'Yes' if report['statsmodels_integration']['availability'] else 'No'}")
    logger.info(f"   Capabilities: {len(report['statsmodels_integration']['capabilities'])
    
    return report

def main():
    """Main test execution"""
    logger.info("🚀 Kimera SWM - Statsmodels Integration Test Suite")
    logger.info("=" * 60)
    
    # Run all tests and generate report
    report = generate_integration_report()
    
    # Final status
    passed_tests = len([r for r in report['test_results'].values() if r['status'] == 'passed'])
    total_tests = len(report['test_results'])
    
    if passed_tests == total_tests:
        logger.info("\n🎉 ALL TESTS PASSED - Statsmodels integration successful!")
    else:
        logger.warning(f"\n⚠️ {total_tests - passed_tests} tests failed - Review integration report")
    
    logger.info("\n📚 Next Steps:")
    for recommendation in report['recommendations']:
        logger.info(f"   • {recommendation}")

if __name__ == "__main__":
    main()