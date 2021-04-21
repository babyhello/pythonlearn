def instructorProfile(id, name, **kwargs):
    print(f"[{id}]instructor:{name} with expertee")
    for k, v in kwargs.items():
        print(f"in {k} field, familiar with {v}")


instructorProfile(1, "Mark")
instructorProfile(2, "Mark", python="Tensorflow", java="Spring")
instructorProfile(3, "Ken", mobile="iOS", server=".NET", os="Linux")
skill = {"js": "Async Programming", "frontend": "React", "cryptoCurrency": "Ethereum"}
instructorProfile(4,"Hawk", **skill)