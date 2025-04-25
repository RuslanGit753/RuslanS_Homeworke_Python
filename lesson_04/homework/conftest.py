import pytest
import time

@pytest.fixture(autouse=True)
def timer():
    start = time.time()
    yield
    end = time.time()
    print(f"\nВремя выполнения теста: {end - start:.2f} seconds")