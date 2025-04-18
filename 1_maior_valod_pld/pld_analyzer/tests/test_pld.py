import pytest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from pld_analyzer.maior_valor_pld import extrair_maximos_submercado_anual

@pytest.fixture
def base_excel_data():
    """Create a base DataFrame for other fixtures"""
    # Create sample data with ME frequency instead of deprecated M
    dates = pd.date_range(start='2023-01-01', periods=4, freq='ME')
    submercados = ['SUDESTE', 'SUL', 'NORDESTE', 'NORTE']
    
    # Create DataFrame with similar structure to PLD.xlsx
    df = pd.DataFrame(index=range(6), columns=['A', 'B'] + list(range(len(dates))))
    
    # Add dates in first row
    df.iloc[0, 2:] = dates
    
    # Add submercados
    df.iloc[1:5, 1] = submercados
    
    # Add random values
    np.random.seed(42)  # for reproducibility
    df.iloc[1:5, 2:] = np.random.uniform(100, 500, size=(4, len(dates)))
    
    return df

@pytest.fixture
def mock_excel_with_nan(base_excel_data):
    """Create a mock DataFrame with NaN values"""
    df = base_excel_data.copy()
    df.iloc[1, 3] = np.nan  # Add NaN in SUDESTE region
    return df

@pytest.fixture
def mock_excel_incomplete_year(base_excel_data):
    """Create a mock DataFrame with missing months"""
    df = base_excel_data.copy()
    # Remove last month
    df = df.iloc[:, :-1]
    return df

def test_basic_functionality(tmp_path, base_excel_data):
    """Test basic functionality with complete data"""
    excel_path = tmp_path / "test_pld.xlsx"
    base_excel_data.to_excel(excel_path, index=False)
    
    resultado = extrair_maximos_submercado_anual(excel_path)
    
    assert len(resultado) > 0
    assert all(col in resultado.columns for col in ['Submercado', 'Ano', 'Valor'])
    assert len(resultado['Submercado'].unique()) == 4
    assert all(resultado['Valor'] >= 0)

def test_nan_values(tmp_path, mock_excel_with_nan):
    """Test handling of NaN values"""
    excel_path = tmp_path / "test_pld_nan.xlsx"
    mock_excel_with_nan.to_excel(excel_path, index=False)
    
    resultado = extrair_maximos_submercado_anual(excel_path)
    
    assert not resultado['Valor'].isna().any()

def test_incomplete_year(tmp_path, mock_excel_incomplete_year):
    """Test handling of incomplete year data"""
    excel_path = tmp_path / "test_pld_incomplete.xlsx"
    mock_excel_incomplete_year.to_excel(excel_path, index=False)
    
    resultado = extrair_maximos_submercado_anual(excel_path)
    
    assert len(resultado) > 0
    assert all(resultado['Valor'] >= 0)

def test_expected_output_structure(tmp_path, base_excel_data):
    """Test if output DataFrame has expected structure and values"""
    excel_path = tmp_path / "test_pld_structure.xlsx"
    base_excel_data.to_excel(excel_path, index=False)
    
    resultado = extrair_maximos_submercado_anual(excel_path)
    
    expected_columns = ['Submercado', 'Ano', 'Valor']
    assert list(resultado.columns) == expected_columns
    
    expected_submercados = ['SUDESTE', 'SUL', 'NORDESTE', 'NORTE']
    assert set(resultado['Submercado'].unique()) == set(expected_submercados)
    
    assert all(resultado['Ano'] == 2023)