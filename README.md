

# **Ogun Library**

![Ogun Library Logo](ogun_logo.png)

The Ogun Library is a versatile risk assessment tool designed to quantify risk in various domains, industries, and contexts. Whether you need to assess financial risk, credit risk, or operational risk, Ogun offers customization, modularity, and default methods to meet your specific risk assessment needs

## **Table of Contents**

- [**Ogun Library**](#ogun-library)
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

The Ogun Library is a versatile risk assessment tool with customization, modularity, and default methods for quantifying risk in various domains.

## **2. Getting Started**

### **Installation**

Provide instructions on how to install the library.

```bash
pip install ogun
```

### **Quick Start**

Certainly! Here's a quick example of how to use the Ogun Library for risk assessment:

Suppose you have the following data for a user:

- `account_balance`: 10
- `account_age`: 5
- `work_status`: 4
- `Salary`: 10

You want to assess the user's risk using the default risk calculation method provided by the Ogun Library.

```python
from ogun import Ogun

# Initialize Ogun
ogun = Ogun()

# Set the user's data for risk assessment
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

# Print the risk assessment
print("Risk Rating:", result.rating)
print("Status:", result.status)
```

In this example:

1. We import the `Ogun` class from the Ogun Library.

2. We initialize the `Ogun` class by creating an instance called `ogun`.

3. We define the user's data as a dictionary with relevant attributes: `account_balance`, `account_age`, `work_status`, and `Salary`.

4. We use the default risk calculation method by chaining method calls to the `ogun` instance. We specify weights for each data attribute using the `.score()` method.

5. Finally, we call the `.get()` method to perform the risk assessment and obtain the result, which includes the risk rating and status.

6. We print the risk assessment result, including the user's risk rating and status.

This is a basic example of how to use the Ogun Library for risk assessment. You can customize the library further by creating custom filters, custom risk calculation methods, and enhancing default methods to meet your specific needs.

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
├── pyproject.toml
├── LICENSE
├── setup.py
├── requirements.txt
├── user_guide.md
└── .gitignore
```

Explanation of the directory structure:

- **ogun/**: The root directory of your Ogun Library.

  - **ogun/**: This subdirectory contains the core code of your library.
    - **__init__.py**: An initialization file for the `ogun` package.
    - **filters/**: Subpackage for custom data filters.
      - **__init__.py**: Initialization file for the filters package.
      - **django_filter.py**: Contains the custom Django ORM filter function.
    - **methods/**: Subpackage for risk calculation methods.
      - **__init__.py**: Initialization file for the methods package.
      - **beta.py**: Implementation of the Beta risk calculation method.
      - **cvar.py**: Implementation of the Conditional Value at Risk (CVaR) method.
      - **default.py**: Default risk calculation methods.
      - **engine.py**: Base class for risk calculation engines.
      - **sharpe.py**: Implementation of the Sharpe Ratio risk calculation method.
      - **st_dev.py**: Implementation of the Standard Deviation risk calculation method.
      - **var.py**: Implementation of the Value at Risk (VaR) risk calculation method.
    - **ogun.py**: The main entry point of your library, where the `Ogun` class is defined.

  - **docs/**: Directory for documentation files.
    - **user_guide.md**: A comprehensive user guide explaining library usage and customization.

  - **examples/**: Directory for example code.
    - **basic.py**: Example code demonstrating basic library usage.

  - **tests/**: Directory for unit tests.
    - **__init__.py**: An initialization file for the tests package.
    - **test_custom_filters.py**: Tests for custom data filters.
    - **test_custom_methods.py**: Tests for custom risk calculation methods.
    - **test_default_methods.py**: Tests for default risk calculation methods.
    - **test_enhance_methods.py**: Tests for enhanced risk calculation methods.
    - **test_ogun.py**: Tests for the core `Ogun` class.
    - **test_utils.py**: Tests for utility functions.

  - **README.md**: Documentation for your library, including project information and an overview.
  - **CODE_OF_CONDUCT.md**: Code of conduct for contributors.
  - **CONTRIBUTING.md**: Guidelines for contributing to the library.
  - **pyproject.toml**: Configuration file for project dependencies and settings (e.g., for using `poetry`).
  - **LICENSE**: The license for your library (e.g., MIT License).
  - **setup.py**: A script for packaging and distributing your library.
  - **requirements.txt**: List of dependencies required to run your library.
  - **user_guide.md**: Comprehensive user guide with detailed explanations and examples.
  - **.gitignore**: File specifying which files or directories should be ignored by version control (e.g., Git).

This directory structure organizes your library into distinct sections, making it easy for users and contributors to navigate and understand. It separates code, documentation, tests, and examples, promoting modularity and maintainability.

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

**1. What is the purpose of the Ogun Library?**
   - The Ogun Library is designed for risk assessment. It enables users to evaluate and quantify risk in various contexts, industries, and domains.

**2. What types of risk can the Ogun Library assess?**
   - Ogun can assess a wide range of risks, including financial risk, credit risk, operational risk, and more. Its flexibility allows users to adapt it to specific risk scenarios.

**3. How does the library handle customization?**
   - Ogun is highly customizable. Users can define their own risk factors, apply custom weights, and create custom risk assessment methods tailored to their needs.

**4. What default risk calculation methods are available?**
   - Ogun provides default methods like Standard Deviation, Value at Risk (VaR), Conditional Value at Risk (CVaR), Sharpe Ratio, Beta, and more, which can be used as starting points for risk assessment.

**5. Can I extend the library's functionality?**
   - Yes, the library is designed for extensibility. You can add custom filters, create custom risk calculation methods, and enhance default methods to meet specific use cases.

**6. Is the library suitable for large datasets?**
   - Yes, Ogun can handle risk assessments for both individual data points and large datasets, making it scalable for various applications.

**7. What types of data sources does the library support?**
   - Ogun is compatible with various data sources and structures, allowing users to adapt it to their specific data requirements.

**8. Is there documentation available for the library?**
   - Yes, the library includes comprehensive documentation, including a user guide, to help users understand its capabilities and conduct risk assessments effectively.

**9. How can I ensure the reliability of risk assessment results?**
   - Ogun incorporates a testing framework to ensure the accuracy and reliability of risk assessment methods.

**10. Is the Ogun Library open-source?**
   - Yes, the library is open-source and can be used and extended by the community.

**11. How can I contribute to the Ogun Library?**
   - You can contribute to the library by following the guidelines provided in the CONTRIBUTING.md file in the repository.

**12. Where can I get support or ask questions about the library?**
   - For support, questions, or discussions, you can refer to the library's GitHub repository.


## **9. Support**

you can refer to the library's GitHub repository issues

## **10. Contributing**

We welcome contributions from the community! Please refer to the [Contributing Guidelines](CONTRIBUTING.md) for information on how to get started, code style, and the contribution process.

## **11. License**

This project is licensed under the [MIT License](LICENSE).

---