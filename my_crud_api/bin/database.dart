import 'package:mysql1/mysql1.dart';

class DatabaseHelper {
  static final DatabaseHelper _instance = DatabaseHelper._internal();
  late MySqlConnection _connection;

  factory DatabaseHelper() {
    return _instance;
  }

  DatabaseHelper._internal();

  Future<void> connect() async {
    _connection = await MySqlConnection.connect(ConnectionSettings(
      host: 'localhost', // آدرس سرور
      port: 3306,        // پورت MySQL
      user: 'root',      // نام کاربری MySQL
      password: null, // رمز عبور
      db: 'crud_database', // نام پایگاه داده
    ));
  }

  MySqlConnection get connection => _connection;

  Future<void> close() async {
    await _connection.close();
  }
}