# ycj_app
This application is a Flask-based web application designed to facilitate manipulation and querying of Excel files. It is particularly focused on managing inventory-related information. Here is a brief summary of its functionalities:

1. **File Selection:** The user can select an Excel file from the 'uploads' directory. This is done through the `choose_file()` route that lists all files in the directory and allows the user to select one.

2. **Sheet Selection:** Once a file is selected, the user can then select a specific sheet within that Excel file. This is handled by the `choose_sheet()` route. 

3. **Data Input:** The user can input data into specific fields (such as 日期, 厂家名称, 项目, 商品名称, 客户, 入库, 出库, 余数, 单位, 单价, 总价, 收入, 利润). This data is appended to the selected Excel sheet. The `input_data()` route handles this process.

4. **Remaining Stock Query:** The user can query the remaining stock of a specific product from a specific factory. The `query_remain()` route is responsible for this function, and it uses the `calc_remain()` function to perform the calculation.

5. **Remaining Stock Update and Display:** After the user inputs data, the remaining stock for the inputted factory and product is updated and displayed. This is also handled within the `input_data()` route. 

6. **Navigation:** After selecting a sheet, the user is presented with two options: Query Remaining Stock, and Update Stock then See Remaining Stock, which lead to different routes.

The templates and routes are designed in a way to allow a smooth navigation flow and a clear visual interface for the user. 

For all these routes and functions, the application utilizes Python's Flask framework for the web interface and backend, and pandas for Excel file and data manipulation.

## 中文项目介绍
该应用程序是一个基于 Flask 的网页应用，专为操作和查询 Excel 文件而设计，尤其专注于管理库存相关信息。以下是其功能的简要概述：

1. **文件选择**：用户可以从 "uploads" 目录中选择一个 Excel 文件。这是通过 `choose_file()` 路由来实现的，该路由列出目录中的所有文件并允许用户选择其中的一个。

2. **表格选择**：一旦选择了文件，用户可以选择该 Excel 文件内的特定表格。这由 `choose_sheet()` 路由处理。

3. **数据输入**：用户可以在特定字段（如日期、厂家名称、项目、商品名称、客户、入库、出库、余数、单位、单价、总价、收入、利润）中输入数据。这些数据将被追加到所选的 Excel 表格中。`input_data()` 路由负责这个过程。

4. **剩余库存查询**：用户可以查询特定厂家的特定产品的剩余库存。`query_remain()` 路由负责这个功能，它使用 `calc_remain()` 函数来执行计算。

5. **剩余库存更新和显示**：在用户输入数据后，输入的厂家和产品的剩余库存将被更新和显示。这也是在 `input_data()` 路由中处理的。

6. **导航**：选择表格后，用户将看到两个选项：查询剩余库存，以及更新库存然后查看剩余库存，它们将引导到不同的路由。

模板和路由的设计使用户能够流畅地导航并清楚地看到用户界面。

在所有这些路由和功能中，应用程序利用了 Python 的 Flask 框架用于网页界面和后端，以及 pandas 用于 Excel 文件和数据操作。