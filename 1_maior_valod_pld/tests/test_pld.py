import pytest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from ..maior_valor_pld import extrair_maximos_submercado_anual

@pytest.fixture
def mock_excel_data():
    """Create a mock DataFrame similar to PLD.xlsx"""
    # Create sample data
    dates = pd.date_range(start='2023-01-01', periods=4, freq='M')
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
def mock_excel_with_nan():
    """Create a mock DataFrame with NaN values"""
    df = mock_excel_data()
    df.iloc[1, 3] = np.nan  # Add NaN in SUDESTE region
    return df

@pytest.fixture
def mock_excel_incomplete_year():
    """Create a mock DataFrame with missing months"""
    df = mock_excel_data()
    # Remove last month
    df = df.iloc[:, :-1]
    return df

def test_basic_functionality(tmp_path, mock_excel_data):
    """Test basic functionality with complete data"""
    # Save mock data to temporary Excel file
    excel_path = tmp_path / "test_pld.xlsx"
    mock_excel_data.to_excel(excel_path, index=False)
    
    # Process the file
    resultado = extrair_maximos_submercado_anual(excel_path)
    
    # Basic assertions
    assert len(resultado) > 0
    assert all(col in resultado.columns for col in ['Submercado', 'Ano', 'Valor'])
    assert len(resultado['Submercado'].unique()) == 4  # Four regions
    assert all(resultado['Valor'] >= 0)  # All values should be positive

def test_nan_values(tmp_path, mock_excel_with_nan):
    """Test handling of NaN values"""
    excel_path = tmp_path / "test_pld_nan.xlsx"
    mock_excel_with_nan.to_excel(excel_path, index=False)
    
    resultado = extrair_maximos_submercado_anual(excel_path)
    
    # NaN values should be skipped, not causing errors
    assert not resultado['Valor'].isna().any()

def test_incomplete_year(tmp_path, mock_excel_incomplete_year):
    """Test handling of incomplete year data"""
    excel_path = tmp_path / "test_pld_incomplete.xlsx"
    mock_excel_incomplete_year.to_excel(excel_path, index=False)
    
    resultado = extrair_maximos_submercado_anual(excel_path)
    
    # Should still process available data
    assert len(resultado) > 0
    assert all(resultado['Valor'] >= 0)

def test_expected_output_structure(tmp_path, mock_excel_data):
    """Test if output DataFrame has expected structure and values"""
    excel_path = tmp_path / "test_pld_structure.xlsx"
    mock_excel_data.to_excel(excel_path, index=False)
    
    resultado = extrair_maximos_submercado_anual(excel_path)
    
    expected_columns = ['Submercado', 'Ano', 'Valor']
    assert list(resultado.columns) == expected_columns
    
    # Test if all submercados are present
    expected_submercados = ['SUDESTE', 'SUL', 'NORDESTE', 'NORTE']
    assert set(resultado['Submercado'].unique()) == set(expected_submercados)
    
    # Test if year is correctly extracted
    assert all(resultado['Ano'] == 2023)