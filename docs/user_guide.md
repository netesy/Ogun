

# **User Guide for Ogun Library**

Welcome to the Ogun Library User Guide! This guide will help you understand how to use the library for risk calculations and how to extend or fine-tune it for your specific needs.

## **Table of Contents**

- [**User Guide for Ogun Library**](#user-guide-for-ogun-library)
  - [**Table of Contents**](#table-of-contents)
  - [**1. Introduction**](#1-introduction)
  - [**2. Getting Started**](#2-getting-started)
    - [**Installation**](#installation)
    - [**Quick Start**](#quick-start)
  - [**3. Library Overview**](#3-library-overview)
    - [**Library Structure**](#library-structure)
  - [**4. Basic Usage**](#4-basic-usage)
    - [**Initializing Ogun**](#initializing-ogun)
    - [**Setting Data**](#setting-data)
    - [**Selecting a Risk Calculation Method**](#selecting-a-risk-calculation-method)
    - [**Scoring Data**](#scoring-data)
    - [**Getting the Risk Rating**](#getting-the-risk-rating)
  - [**5. Extending the Library**](#5-extending-the-library)
    - [**Adding Custom Risk Calculation Methods**](#adding-custom-risk-calculation-methods)
    - [**Creating Custom Filters**](#creating-custom-filters)
    - [**Enhancing the Default Risk Calculation Method**](#enhancing-the-default-risk-calculation-method)
  - [**6. Advanced Usage**](#6-advanced-usage)
    - [**Handling Exceptions**](#handling-exceptions)
    - [**Customizing Risk Rating Thresholds**](#customizing-risk-rating-thresholds)
  - [**7. Examples**](#7-examples)
    - [**Example 1: Using a Custom Risk Calculation Method**](#example-1-using-a-custom-risk-calculation-method)
    - [**Example 2: Customizing Thresholds**](#example-2-customizing-thresholds)
  - [**8. FAQs**](#8-faqs)
  - [**9. Support**](#9-support)
  - [**10. Contributing**](#10-contributing)
  - [**11. License**](#11-license)



## **1. Introduction**

Introduce the Ogun Library, its purpose, and its capabilities.

## **2. Getting Started**

### **Installation**

Provide instructions on how to install the library.

```bash
pip install ogun
```

### **Quick Start**

Show a quick example of how to use the library to calculate risk.

## **3. Library Overview**

### **Library Structure**

Creating a comprehensive library structure requires organizing your code and files in a clear and maintainable manner. Here's a suggested directory structure for your Ogun Library:

```
ogun/
│
├── ogun/
│   ├── __init__.py
│   ├── filters/
│   │   ├── __init__.py
│   │   └── django_filter.py
│   ├── methods/
│   │   ├── __init__.py
│   │   ├── beta.py
│   │   ├── cvar.py
│   │   ├── default.py
│   │   ├── engine.py
│   │   ├── sharpe.py
│   │   ├── st_dev.py
│   │   └── var.py
│   └── ogun.py
│
├── docs/
│   └── user_guide.md
│
├── examples/
│   └── basic.py
│
├── tests/
│   ├── __init__.py
│   ├── test_custom_filters.py
│   ├── test_custom_methods.py
│   ├── test_default_methods.py
│   ├── test_enhance_methods.py
│   ├── test_ogun.py
│   └── test_utils.py
│
├── README.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── setup.py
├── requirements.txt
├── user_guide.md
└── .gitignore
```

Explanation of the directory structure:

- **ogun/**: The root directory of your library.
  - **ogun/**: This subdirectory contains the core code of your library.
    - **__init__.py**: An initialization file for the `ogun` package.
    - **filters/**: Subpackage for custom data filters.
      - **__init__.py**: Initialization file for the filters package.
      - **custom_filters.py**: Contains custom data filter functions.
      - **other_filters.py**: Additional built-in data filter functions.
    - **methods/**: Subpackage for custom and enhanced risk calculation methods.
      - **__init__.py**: Initialization file for the methods package.
      - **custom_methods.py**: Contains custom risk calculation methods.
      - **default_methods.py**: Contains default risk calculation methods.
      - **enhance_methods.py**: Contains enhanced risk calculation methods.
    - **utils/**: Subpackage for utility functions and helper modules.
      - **__init__.py**: Initialization file for the utils package.
      - **helper_functions.py**: Contains utility functions.
    - **ogun.py**: The main entry point of your library, where the `Ogun` and `RiskResult` classes are defined.
    - **risk_result.py**: Defines the `RiskResult` class for risk assessment results.
  - **tests/**: Directory for unit tests.
    - **__init__.py**: An initialization file for the tests package.
    - **test_custom_filters.py**: Tests for custom filter functions.
    - **test_custom_methods.py**: Tests for custom risk calculation methods.
    - **test_default_methods.py**: Tests for default risk calculation methods.
    - **test_enhance_methods.py**: Tests for enhanced risk calculation methods.
    - **test_ogun.py**: Tests for the core `Ogun` class.
    - **test_utils.py**: Tests for utility functions.
  - **README.md**: Documentation for your library, including usage instructions and examples.
  - **LICENSE**: The license for your library (e.g., MIT License).
  - **setup.py**: A script for packaging and distributing your library.
  - **requirements.txt**: List of dependencies required to run your library.
  - **user_guide.md**: Comprehensive user guide with detailed explanations and examples.
  - **.gitignore**: File specifying which files or directories should be ignored by version control (e.g., Git).

This directory structure keeps your library organized, making it easier for users and contributors to understand, extend, and maintain. It separates different components, such as filters, methods, and tests, into distinct subdirectories, promoting modular and maintainable code.

---

## **4. Basic Usage**

### **Initializing Ogun**

To use the library, create an instance of the `Ogun` class:

```python
from ogun import Ogun

ogun = Ogun()
```

### **Setting Data**

Set the data for risk assessment using a dictionary:

```python
data = {
    "account_balance": 10,
    "account_age": 5,
    "work_status": 4,
    "Salary": 10,
}

ogun.data(data)
```

### **Selecting a Risk Calculation Method**

Choose a risk calculation method. If no method is specified, the default method is used.

```python
# Use the default method
ogun.using()
```

### **Scoring Data**

Assign scores to data points using the `score` method:

```python
ogun.score("account_balance", 10)
ogun.score("account_age", 5)
ogun.score("work_status", 4)
ogun.score("Salary", 10)
```

### **Getting the Risk Rating**

Calculate risk and retrieve the risk rating and status:

```python
result = ogun.get()

print("Risk Rating:", result.rating)
print("Status:", result.status)
```

---

## **5. Extending the Library**

### **Adding Custom Risk Calculation Methods**

Custom risk calculation methods extend the capabilities of the Ogun Library by allowing you to define your own risk assessment algorithms. You can create custom methods to take into account domain-specific factors or unique data sources. Here's how to create custom risk calculation methods:

**Example: Custom Risk Calculation Method for Finance Industry**

```python
# Import necessary modules
from ogun import Engine

# Define a custom risk calculation class
class CustomFinanceRiskCalculator(Engine):
    def calculate(self):
        # Implement your custom risk calculation logic here
        pass
```

In this example, we create a custom risk calculation method tailored to the finance industry. You can implement your own logic inside the `calculate` method to factor in additional financial metrics or industry-specific considerations.

To use the custom risk calculation method:

```python
# Use the custom risk calculation method with your Ogun instance
result = ogun.data(data).using(CustomFinanceRiskCalculator).get()
```

### **Creating Custom Filters**

Custom filters allow you to apply domain-specific rules and criteria to your data before calculating risk. They enable you to preprocess and manipulate the data to ensure that the risk assessment is tailored to your specific requirements. Here's how to create custom filters:

**Example: Custom Filter to Exclude Data Points Below a Threshold**

```python
# Define a custom filter function
def custom_filter(data, threshold):
    filtered_data = {key: value for key, value in data.items() if value >= threshold}
    return filtered_data
```

In this example, the `custom_filter` function filters out data points with values below a specified threshold. You can create similar custom filter functions to address specific data preprocessing needs in your risk assessment.

To use the custom filter:

```python
# Apply the custom filter to your data
filtered_data = custom_filter(data, threshold=5)

# Use the filtered data in your Ogun library instance
ogun.data(filtered_data)
```

### **Enhancing the Default Risk Calculation Method**

Enhancing default risk calculation methods allows you to modify or extend the built-in risk assessment algorithms to better suit your specific use cases. You might want to add additional data processing steps, custom scoring rules, or other modifications to improve the accuracy of your risk assessments. Here's how to enhance default risk calculation methods:

**Example: Enhancing the Default Risk Calculation Method**

```python
# Import necessary modules
from ogun import Engine, StandardDeviation

# Define a custom risk calculation class that extends the default method
class EnhancedRiskCalculator(StandardDeviation):
    def calculate(self):
        # Add custom processing or scoring logic here
        # You can call the parent class's calculate method to retain default behavior
        default_score = super().calculate()

        # Implement custom modifications
        custom_score = default_score + additional_score

        return custom_score
```

In this example, we create an `EnhancedRiskCalculator` class that extends the default `StandardDeviation` risk calculation method. You can override the `calculate` method to add custom processing or scoring logic while still leveraging the default behavior when necessary.

To use the enhanced risk calculation method:

```python
# Use the enhanced risk calculation method with your Ogun instance
result = ogun.data(data).using(EnhancedRiskCalculator).get()
```

By enhancing default risk calculation methods, you can fine-tune the risk assessment process to better align with your specific business requirements or industry standards.

These examples demonstrate how to create custom filters, custom risk calculation methods, and enhance default risk calculation methods within the Ogun Library, allowing you to tailor risk assessments to your unique needs..

---

## **6. Advanced Usage**

### **Handling Exceptions**
Here's an example of how to use error handling when using your `Ogun` library:

```python
from ogun import Ogun

# Initialize Ogun
ogun = Ogun()

# Set data for risk assessment
data = {
    "account_balance": 10,
    "account_age": 5,
    "work_status": 4,
    "Salary": 10,
}

try:
    # Use the default risk calculation method
    result = (
        ogun.data(data)
        .using()
        .score("account_balance", 10)
        .score("account_age", 5)
        .score("work_status", 4)
        .score("Salary", 10)
        .get()
    )

    # Print the risk assessment
    print("Risk Rating:", result.rating)
    print("Status:", result.status)
except RuntimeError as e:
    # Handle the error gracefully
    print(f"Error: {str(e)}")
```

In this code, we wrap the usage of the `Ogun` library in a `try` block, and if any exceptions occur during risk calculation, we catch them and print a custom error message. This ensures that your application can handle errors without crashing.

### **Customizing Risk Rating Thresholds**

To customize the risk rating thresholds, you can modify the `RiskResult` class file as follows:

```python
# In ogun.py

class RiskResult:
    def __init__(self, total_score):
        self.total_score = total_score

    # Customize the risk rating thresholds
    @property
    def rating(self):
        if self.total_score <= 10:
            return "Very Low Risk"
        elif self.total_score <= 20:
            return "Low Risk"
        elif self.total_score <= 40:
            return "Moderate Risk"
        elif self.total_score <= 60:
            return "High Risk"
        else:
            return "Very High Risk"

    @property
    def status(self):
        return "Approved" if self.rating in ["Very Low Risk", "Low Risk"] else "Denied"
```

In this modified [`RiskResult`](#example-1-using-a-custom-risk-calculation-method-) class, we have adjusted the thresholds for different risk ratings. For example, a total score of up to 10 is now classified as "Very Low Risk," and the thresholds for other risk ratings have also been adjusted accordingly.

---

## **7. Examples**

Provide practical examples demonstrating various library features.

### **Example 1: Using a Custom Risk Calculation Method** 

Customizing the `RiskResult` class in your Ogun Library allows you to define your own criteria for risk rating and status based on the calculated risk score. To do this, you can subclass the `RiskResult` class and override its methods to implement your custom logic. Below, I'll provide an example of how you can customize the `RiskResult` class with code and an example scenario.

**Customizing the RiskResult Class**

First, let's create a custom `RiskResult` class with custom rating and status logic:

```python
from ogun import RiskResult

class CustomRiskResult(RiskResult):
    def __init__(self, total_score):
        super().__init__(total_score)

    @property
    def rating(self):
        if self.total_score <= 20:
            return "Very Low Risk"
        elif self.total_score <= 40:
            return "Low Risk"
        elif self.total_score <= 60:
            return "Moderate Risk"
        elif self.total_score <= 80:
            return "High Risk"
        else:
            return "Very High Risk"

    @property
    def status(self):
        if self.rating in ["Very Low Risk", "Low Risk"]:
            return "Approved"
        else:
            return "Denied"
```

In this example, we've created a custom `CustomRiskResult` class that inherits from the `RiskResult` class and overrides the `rating` and `status` properties. The custom rating logic categorizes risk into five categories, and the custom status logic approves applications with "Very Low Risk" or "Low Risk" ratings and denies others.

**Using the Custom RiskResult Class**

Now, let's use this custom `CustomRiskResult` class in your Ogun code:

```python
from ogun import Ogun

# Initialize Ogun
ogun = Ogun()

# Set data for risk assessment
data = {
    "account_balance": 10,
    "account_age": 5,
    "work_status": 4,
    "Salary": 10,
}

# Use the default risk calculation method
result = (
    ogun.data(data)
    .using()
    .score("account_balance", 10)
    .score("account_age", 5)
    .score("work_status", 4)
    .score("Salary", 10)
    .get()
)

# Use the custom RiskResult class
custom_result = CustomRiskResult(result.total_score)

print("Custom Risk Rating:", custom_result.rating)
print("Custom Status:", custom_result.status)
```

In this code, we create an instance of the `CustomRiskResult` class based on the result obtained from the default risk calculation. This allows us to apply our custom risk rating and status logic to the same risk assessment.

This example demonstrates how you can customize the `RiskResult` class to implement your own risk rating and status criteria to fit specific business requirements or risk assessment scenarios.

### **Example 2: Customizing Thresholds**

Check out Customising RiskResult Class

---

## **8. FAQs**

Answer frequently asked questions about the library.

## **9. Support**

Provide contact information for user support and assistance.

## **10. Contributing**

We welcome contributions from the community! Please refer to the [Contributing Guidelines](CONTRIBUTING.md) for information on how to get started, code style, and the contribution process.

## **11. License**

This project is licensed under the [MIT License](LICENSE).

---