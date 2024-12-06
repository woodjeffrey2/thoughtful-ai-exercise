from enum import Enum, auto

# Define an enum class to represent the package type
class PackageType(str, Enum):
  STANDARD = 'STANDARD'
  SPECIAL = 'SPECIAL'
  REJECTED = 'REJECTED'

# Function to sort the package based on its width, height, length, and mass
def sort(width, height, length, mass):
  if not all(isinstance(i, (int, float)) for i in [width, height, length, mass]):
      raise TypeError('Width, height, length, and mass must be numbers')
  if not all(i > 0 for i in [width, height, length, mass]):
      raise ValueError('Width, height, length, and mass must be greater than 0')
  isBulky = width * height * length > 150
  isHeavy = mass > 20
  if isBulky and isHeavy:
    return PackageType.REJECTED
  if isHeavy or isBulky:
    return PackageType.SPECIAL
  return PackageType.STANDARD

# Test cases
assert sort(10, 10, 1, 10) == 'STANDARD', \
  'Should return STANDARD package type when not bulky or heavy'
assert sort(10, 10, 10, 10) == 'SPECIAL', \
  'Should return SPECIAL package type when bulky but not heavy'
assert sort(10, 10, 1, 30) == 'SPECIAL', \
  'Should return SPECIAL package type when heavy but not bulky'
assert sort(10, 10, 10, 30) == 'REJECTED', \
  'Should return REJECTED package type when both bulky and heavy'
assert sort(10.0, 10.0, 1.0, 10.5) == 'STANDARD', \
  'Should handle float numbers'
try:
  result = sort(10, 10, 1, '10')
  assert False, 'Should raise TypeError when mass is not a number'
except TypeError as e:
  assert str(e) == 'Width, height, length, and mass must be numbers', \
    'Should raise TypeError when width, height, length, or mass is not a number'
try:
  result = sort(0, 10, 1, 10)
  assert False, 'Should raise ValueError when width is 0'
except ValueError as e:
  assert str(e) == 'Width, height, length, and mass must be greater than 0', \
    'Should raise ValueError when width is 0'
