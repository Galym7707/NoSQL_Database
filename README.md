Код файла all code.py реализовывает класс NoSQL Database. Ниже представлено подробное описание класса Database



init(self, db_name: str) - инициализирует объект базы данных и создает словарь для таблиц.
create_table(self, table_name: str, columns: Dict[str, str], primary_key: str) - создает новую таблицу с заданным именем, столбцами и первичным ключом и добавляет ее в словарь таблиц.
add_row(self, table_name: str, row: Dict[str, Any]) - добавляет новую строку в заданную таблицу.
update_row(self, table_name: str, row_id: Any, updates: Dict[str, Any]) - обновляет заданную строку в заданной таблице.
delete_row(self, table_name: str, row_id: Any) - удаляет заданную строку из заданной таблицы.
get_rows(self, table_name: str, filters: List[Dict[str, Any]], sort_by: str = None, desc: bool = False) - получает все строки из заданной таблицы, которые соответствуют заданным фильтрам и сортирует их по заданному столбцу, если указано.
filter_rows(self, rows: List[Dict[str, Any]], filters: List[Dict[str, Any]]) -> List[Dict[str, Any]] - фильтрует заданные строки таблицы по заданным фильтрам.
sort_rows(self, rows: List[Dict[str, Any]], sort_by: str, desc: bool = False) -> List[Dict[str, Any]] - сортирует заданные строки таблицы по заданному столбцу.
get_row_by_id(self, table: Dict[str, Any], row_id: Any) -> Dict[str, Any] - получает строку из заданной таблицы по заданному первичному ключу.
validate_row(self, row: Dict[str, Any], table: Dict[str, Any]) -> bool - проверяет, соответствует ли заданная строка таблицы заданным столбцам и ограничениям.
save(self) - сохраняет словарь таблиц в формате JSON.
load(self) - загружает словарь таблиц из файла JSON с заданным именем.
