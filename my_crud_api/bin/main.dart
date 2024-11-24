import 'dart:convert';
import 'package:shelf/shelf.dart';
import 'package:shelf/shelf_io.dart' as io;
import 'package:shelf_router/shelf_router.dart';
import 'database.dart';

final dbHelper = DatabaseHelper();

Response _jsonResponse(Map<String, dynamic> data) =>
    Response.ok(jsonEncode(data), headers: {'Content-Type': 'application/json'});

final router = Router()
  // مسیر ایجاد (Create)
  ..post('/items', (Request req) async {
    final payload = await req.readAsString();
    final data = jsonDecode(payload);

    final result = await dbHelper.connection.query(
        'INSERT INTO items (name, description) VALUES (?, ?)',
        [data['name'], data['description']]);

    return _jsonResponse({
      'message': 'Item created successfully!',
      'insertedId': result.insertId
    });
  })
  // مسیر دریافت همه (Read)
  ..get('/items', (Request req) async {
    final results = await dbHelper.connection.query('SELECT * FROM items');
    final items = results
        .map((row) => {
              'id': row['id'],
              'name': row['name'],
              'description': row['description']
            })
        .toList();

    return _jsonResponse({'items': items});
  })
  // مسیر به‌روزرسانی (Update)
  ..put('/items/<id>', (Request req, String id) async {
    final payload = await req.readAsString();
    final data = jsonDecode(payload);

    await dbHelper.connection.query(
        'UPDATE items SET name = ?, description = ? WHERE id = ?',
        [data['name'], data['description'], int.parse(id)]);

    return _jsonResponse({'message': 'Item updated successfully!'});
  })
  // مسیر حذف (Delete)
  ..delete('/items/<id>', (Request req, String id) async {
    await dbHelper.connection.query('DELETE FROM items WHERE id = ?', [int.parse(id)]);

    return _jsonResponse({'message': 'Item deleted successfully!'});
  });

void main() async {
  // اتصال به پایگاه داده
  await dbHelper.connect();

  final handler = const Pipeline()
      .addMiddleware(logRequests())
      .addHandler(router);

  final server = await io.serve(handler, 'localhost', 8080);
  print('Server running at http://${server.address.host}:${server.port}');
}