# Thoughtful Robotic automation factory sorting

This project implements a package sorting function for Thoughtful's robotic automation factory. The function dispatches packages to the correct stack based on their volume and mass.

## Function Description

The `sort` function takes four parameters:

- `width`: Width of the package in centimeters
- `height`: Height of the package in centimeters
- `length`: Length of the package in centimeters
- `mass`: Mass of the package in kilograms

It returns a string indicating the appropriate stack for the package:

- "STANDARD": For packages that are neither bulky nor heavy
- "SPECIAL": For packages that are either bulky or heavy
- "REJECTED": For packages that are both bulky and heavy

## Sorting Criteria

- A package is **bulky** if:
  - Its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³, or
  - Any of its dimensions is greater than or equal to 150 cm
- A package is **heavy** if its mass is greater than or equal to 20 kg

## Implementation

```python
def sort(width, height, length, mass):
    volume = width * height * length
    is_bulky = volume >= 1000000 or max(width, height, length) >= 150
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
```

## Test Cases

The implementation includes a `run_tests` function that executes several test cases to verify the correctness of the `sort` function. These test cases cover various scenarios, including:

- Standard packages
- Bulky packages (due to volume and dimensions)
- Heavy packages
- Rejected packages
- Edge cases (e.g., zero dimensions and mass)

## Running the Code

You can run this code using an online Python IDE like PyCharm.

Click the "Run" button to execute the code and see the test results. For easier viewing the output from my local editor is pasted at the end of code file.

## Features

- **Correct sorting logic**: Implements the given criteria for bulky and heavy packages accurately
- **Code quality**: Clean, well-commented, and easy to understand
- **Handling edge cases**: Includes test cases for various scenarios, including edge cases
- **Comprehensive test coverage**: Covers all package types and sorting outcomes

Feel free to review the code, run the tests, and let me know if you have any questions or suggestions for improvements!

Citations:
[1] https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
[2] https://www.nobledesktop.com/learn/git/create-a-readme-file
[3] https://www.sitepoint.com/github-profile-readme/
[4] https://stackoverflow.com/questions/44290660/how-to-create-a-readme-file-inside-a-subdirectory-on-github/44290875
[5] https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme
[6] https://www.youtube.com/watch?v=QcZKsbgsLa4
[7] https://www.makeareadme.com
[8] https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/
