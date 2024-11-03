void main() {
  List<Map<String, dynamic>> data = [
    {'id': 1, 'name': 'Alice', 'score': 3},
    {'id': 2, 'name': 'Bob', 'score': 7.87},
    {'id': 3, 'name': 'Charlie', 'score': 9.001},
    {'id': 4, 'name': 'David', 'score': 11},
    {'id': 5, 'name': 'Eve', 'score': 13},
    {'id': 6, 'name': 'Frank', 'score': 8},
    {'id': 7, 'name': 'Grace', 'score': 9},
    {'id': 8, 'name': 'Hannah', 'score': 9.2},
    {'id': 9, 'name': 'Isaac', 'score': 8.86},
  ];

  List<Map<String, dynamic>> arryNewData = [];

  data.forEach((stu) {
    arryNewData.add({
      'score': (stu['score'] as double).ceil(),
      'status': stu['score'] > 9 ? 'pass' : 'faild',
    });

    // Uncomment the following lines for the second approach
    // double scoreTest = stu['score'] % 1 > 0.5 ? (stu['score'] + 1).floorToDouble() : stu['score'].floorToDouble();
    // arryNewData.add({'score': scoreTest, 'status': stu['score'] >= 10 ? 'pass' : 'faild'});
  });

  print(arryNewData);
}
