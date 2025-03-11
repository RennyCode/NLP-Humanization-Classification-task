# Text Humanization Rules Tests

This directory contains test files for each of the text humanization rules. The tests verify that both the fix functions (which apply the transformations) and score functions (which measure the presence of specific text characteristics) work correctly.

## Running the Tests with pytest

You can run all tests using pytest:

```bash
# From the project root
pytest

# With more verbose output
pytest -v

# Run a specific test file
pytest tests/test_capitalization.py

# Run tests matching a pattern
pytest -k "emoji"

# Generate coverage report
pytest --cov=rules
```

## Test Styles

The test suite includes two types of test files:

1. **Unittest-style tests**: 
   - Class-based tests inheriting from `unittest.TestCase`
   - Using assertions like `self.assertEqual()`, `self.assertTrue()`
   
2. **Pytest-style tests**:
   - Function-based tests without a class
   - Using simple assertions like `assert value == expected`
   - Example: `test_ai_mentions_pytest.py`

For new tests, we recommend using the pytest style as it's more concise and readable. You can use the `pytest_template.py` file as a starting point.

## Test Structure

Each test file includes tests for:

1. **Fix function tests**: Testing the transformation logic
2. **Score function tests**: Testing the measurement logic
3. **Edge case tests**: Testing behavior with empty strings, etc.
4. **Random seed tests**: For rules with probabilistic elements

## Adding New Tests

To add tests for a new rule:

1. Create a new file named `test_rulename.py`
2. Use the pytest style from `pytest_template.py` as a guide
3. Implement tests for:
   - Basic functionality of the fix function
   - Edge cases (empty strings, already-formatted text, etc.)
   - Score function accuracy
   - Reproducibility (using fixed random seeds)

## Advanced pytest Features

Pytest offers several advanced features:

1. **Parametrized tests**: Test multiple inputs with a single test function
   ```python
   @pytest.mark.parametrize("input_text,expected", [
       ("input1", "expected1"),
       ("input2", "expected2"),
   ])
   def test_function(input_text, expected):
       assert fix_function(input_text) == expected
   ```

2. **Fixtures**: For setup and teardown
   ```python
   @pytest.fixture
   def seed_random():
       random.seed(42)
       yield
       random.seed(None)
   
   def test_with_fixture(seed_random):
       # Test with fixed random seed
   ```

3. **Custom markers**: For categorizing tests
   ```python
   @pytest.mark.slow
   def test_slow_function():
       # Run with: pytest -m slow
   ```

## Troubleshooting

If tests fail unexpectedly:

1. Check if the rule implementation has changed
2. Verify that random seeds are being set correctly for probabilistic rules
3. Check your Python version (Python 3.6+ required)
4. Use `pytest -v` or `pytest -vv` for more detailed output 