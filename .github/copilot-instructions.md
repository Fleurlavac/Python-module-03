# Python Module 03: Data Quest - AI Coding Agent Instructions

## Project Overview

**Data Quest: The Pixel Dimension** is an educational Python module teaching data structures, algorithms, and command-line interaction through a gaming analytics theme. The codebase contains interactive exercises where learners work with player scores, achievements, and game coordinates.

### Architecture & Key Components

- **`data_generator.py`**: Central unified data generator using dispatch pattern (Exercise 0-6 support). `PixelDataGenerator` class abstracts data generation across all exercises with seeded randomness for reproducible test data.
- **`advanced_data_helper.py`**: Advanced utilities for edge cases, nested data structures, and performance testing scenarios.
- **`exercise_*_helper.py`**: Teaching aids explaining concepts (command-line args, list operations, etc.) with discovery hints.
- **Exercise files** (`ft_*.py`): Self-contained implementations demonstrating core concepts:
  - `ft_command_quest.py`: Command-line argument handling via `sys.argv`
  - `ft_score_analytics.py`: List aggregation and statistical analysis
  - `ft_coordinate_system.py`: 3D distance calculations and tuple unpacking
  - `ft_achievement_tracker.py`: Set operations (union, intersection, difference)

## Data Flows & Patterns

### Gaming Theme Domain Model
- **Players**: Named entities with achievement sets and scores
- **Achievements**: Badges from `first_kill` to `completionist` (16 total)
- **Items**: Typed inventory (weapons, consumables, materials) with rarity levels
- **Scores**: Player performance metrics from 0-3500+ depending on archetype and game mode

### Key Conventions
1. **Dispatch Pattern** (see `data_generator.py`): Generator methods mapped by exercise number enables clean separation of concern
2. **Seeded Randomness**: Always initialize `random.seed()` for deterministic output (critical for testing)
3. **Type Hints**: Files use `typing` module annotations (`List[int]`, `Dict[str, Any]`, etc.)
4. **Functional Approach**: Utility files expose functions at module level; classes provide organized method grouping
5. **Gaming Lexicon**: Use domain terms (archetype, multiplier, variance, mode) consistently

## Developer Workflows

### Running Exercises
```bash
python3 ft_command_quest.py arg1 arg2 arg3          # Prints sys.argv inspection
python3 ft_score_analytics.py 100 200 300           # Analytics on command args
python3 ft_coordinate_system.py                     # 3D geometry demo
python3 ft_achievement_tracker.py                   # Interactive player achievements
```

### Generating Test Data
```python
from data_generator import PixelDataGenerator
gen = PixelDataGenerator(seed=42)
scores = gen.generate_exercise_data(1, count=10)    # 10 scores for analytics
```

### Helper Discovery
Each helper file explains foundational concepts—refer to `exercise_*_help.py` when adding new tutorials.

## Critical Patterns to Preserve

1. **File Header Format**: All `.py` files use 42-school header (UTF-8 box art with timestamps)
2. **Exercise Dispatch**: New exercises integrate via `PixelDataGenerator.generate_exercise_data()` method
3. **Error Handling**: Use try/except for `ValueError` in parsing (see `ft_coordinate_system.py`)
4. **Set Operations**: Use built-in set methods (`.union()`, `.intersection()`, `-` operator) for achievement logic
5. **Tuple Unpacking**: Leverage Python's unpacking for coordinate/vector operations: `x, y, z = coordinates`

## Integration Points

- **External Dependencies**: Only standard library (`sys`, `math`, `random`, `typing`, `statistics`)
- **No file I/O**: All data passed via command-line arguments or in-memory structures
- **Output Format**: Use emoji-enhanced print statements for visual feedback (🌟, ⚔️, 👑, etc.)

## Common Extensions

When adding new exercises:
1. Add player archetype/game mode config to `ScoreAnalyticsGenerator` in `exercise_1_helper.py`
2. Register generator method in `PixelDataGenerator.generate_exercise_data()` dispatch dict
3. Create `ft_<concept>.py` with main logic + `if __name__ == "__main__":` entry point
4. Document in corresponding `exercise_<num>_help.py` with discovery hints
