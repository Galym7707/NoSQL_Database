import json
import os 
from decimal import Decimal
from typing import List, Dict, Any

class Database:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.tables = {}

    def create_table(self, table_name: str, columns: Dict[str, str], primary_key: str):
        table = {"columns": columns, "primary_key": primary_key, "data": []}
        self.tables[table_name] = table
        self.save()

    def add_row(self, table_name: str, row: Dict[str, Any]):
        table = self.tables[table_name]
        if not self.validate_row(row, table):
            return False
        table["data"].append(row)
        self.save()
        return True

    def update_row(self, table_name: str, row_id: Any, updates: Dict[str, Any]):
        table = self.tables[table_name]
        row = self.get_row_by_id(table, row_id)
        if not row:
            return False
        for key, value in updates.items():
            if key != table["primary_key"]:
                row[key] = value
        self.save()
        return True

    def delete_row(self, table_name: str, row_id: Any):
        table = self.tables[table_name]
        row = self.get_row_by_id(table, row_id)
        if not row:
            return False
        table["data"].remove(row)
        self.save()
        return True

    def get_rows(self, table_name: str, filters: List[Dict[str, Any]], sort_by: str = None, desc: bool = False):
        table = self.tables[table_name]
        filtered_rows = self.filter_rows(table["data"], filters)
        sorted_rows = self.sort_rows(filtered_rows, sort_by, desc)
        return sorted_rows

    def filter_rows(self, rows: List[Dict[str, Any]], filters: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        filtered_rows = []
        for row in rows:
            matches_all_filters = True
            for filter in filters:
                column = filter["column"]
                value = filter["value"]
                if row.get(column) != value:
                    matches_all_filters = False
                    break
            if matches_all_filters:
                filtered_rows.append(row)
        return filtered_rows

    def sort_rows(self, rows: List[Dict[str, Any]], sort_by: str, desc: bool = False) -> List[Dict[str, Any]]:
        if not sort_by:
            return rows
        sorted_rows = sorted(rows, key=lambda row: row[sort_by], reverse=desc)
        return sorted_rows

    def get_row_by_id(self, table: Dict[str, Any], row_id: Any) -> Dict[str, Any]:
        for row in table["data"]:
            if row[table["primary_key"]] == row_id:
                return row
        return None

    def validate_row(self, row: Dict[str, Any], table: Dict[str, Any]) -> bool:
        for column, column_type in table["columns"].items():
            if column not in row:
                return False
            if row[column] is None and "not null" in column_type:
                return False
        return True

    def save(self):
        with open(f"{self.db_name}.json", "w") as f:
            json.dump(self.tables, f, indent=4)

    def load(self):
        try:
            with open(f"{self.db_name}.json
                      
class DataType:
    #Типы данных в таблицах
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def validate(self, value):
        #Метод, проверяющий соответствие значения определенному типу данных
        raise NotImplementedError


class IntType(DataType):
    #тип данных Int
    def validate(self, value):
        if not isinstance(value, int):
            raise ValueError(f"{value} is not an integer")
        return True


class StrType(DataType):
    #тип данных String
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{value} is not a string")
        return True


class URLType(DataType):
    #тип данных url
    def validate(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{value} is not a string")
        if not value.startswith("http"):
            raise ValueError(f"{value} is not a valid URL")
        return True


class FloatType(DataType):
    #тип данных float
    def validate(self, value):
        if not isinstance(value, float):
            raise ValueError(f"{value} is not a float")
        return True


class DecimalType(DataType):
    #тип данных decimal
    def validate(self, value):
        if not isinstance(value, decimal.Decimal):
            raise ValueError(f"{value} is not a decimal")
        return True


class Constraint:
    #ограничения на поля таблиц
    def __init__(self, field_name):
        self.field_name = field_name

    def validate(self, value):
        """
        Метод, проверяющий соответствие значения ограничению
        """
        raise NotImplementedError


class NotNull(Constraint):
    #ограничение NOT NULL
    def validate(self, value):
        if value is None:
            raise ValueError(f"{self.field_name} cannot be null")
        return True


class PrimaryKey(Constraint):
    #ограничение PRIMARY KEY
    def __init__(self, field_name):
        super().__init__(field_name)
        self.values = set()

    def validate(self, value):
        if value in self.values:
            raise ValueError(f"{value} already exists in primary key {self.field_name}")
        self.values.add(value)
        return True
