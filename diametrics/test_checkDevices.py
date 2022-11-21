from unittest.mock import patch, MagicMock

from checkDevices import preprocessing

# Unit tests for checkDevices

# Testig preprocessing class
# Should probably be renamed Preprocessing - classes

@patch('checkDevices.preprocessing.assert_flash_libre')
def test_preprocessing_1(mock_assert_flash_libre: MagicMock):

    #mock_assert_flash_libre.return_value = False
    df = MagicMock()
    instance = preprocessing(df)
    mock_assert_flash_libre.assert_called()


@patch('checkDevices.preprocessing.assert_flash_libre', return_value=False)
@patch('checkDevices.preprocessing.convert_flash_libre')
@patch('checkDevices.preprocessing.autoprocess')
def test_preprocessing_2(mock_assert_flash_libre: MagicMock,
                         mock_convert_flash_libre: MagicMock,
                         mock_autoprocess: MagicMock):

    df = MagicMock()
    instance = preprocessing(df)
    mock_convert_flash_libre.assert_not_called()
