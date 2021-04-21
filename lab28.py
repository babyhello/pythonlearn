def variable28(id, name, *courses):
    print(f"student id={id}, name={name}, attend python courses:")
    for c in courses:
        print("course:%s" % str(c))


variable28(1, "Mark")
variable28(2, "John", "Python")
variable28(3, "Tim", "Pandas", "Numpy")
variable28(4, "Mary", "OpenVino", "YOLO", "RCNN")
variable28(4, "Mary", ("OpenVino", "YOLO", "RCNN"))
variable28(4, "Mary", *("OpenVino", "YOLO", "RCNN"))