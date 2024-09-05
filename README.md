# sql-generator

## The purpose

This code is used to create SQL statementes bases on excel files.

You just need to set the path of the target file and select between insert, delete and update statements.
For additional help, all the infos you need to know are found bellow.

### Insert
Call the function **insert_generator** with the following arguments:

1. **df** - your pandas dataframe;
2. **table_name** - your SQL table name, where the data will be inserted;
3. **file_name** - the name you desire your SQL file will have after done;
4. **step** (optional) - splits your excel file in smaller files with 'step' rows. This generates multiple SQL statements, based on the numbers of rows will need.

### Delete
In future versions.

### Update
In future versions.

<br /><br />
Feel free to send sugestions!
