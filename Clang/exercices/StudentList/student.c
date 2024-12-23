
enum Sex { SEX_F, SEX_M };

typedef struct {
  int mark;
  struct MarkNode *next;
} MarkNode;

typedef struct {
  int id, age;
  enum Sex sex;
  MarkNode *marks;
  char name[];
} Student;

typedef struct {
  struct StudentNode *next;
  Student student;
} StudentNode;
