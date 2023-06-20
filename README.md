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