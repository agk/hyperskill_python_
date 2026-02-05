def congratulations(manager_name, testing_name, *developer):
    message = "Happy New Year! Take care of yourself and your loved ones!\nFor:\n"
    message += manager_name + "\n"
    message += testing_name + "\n"

    for name in developer:
        message += name + "\n"

    print(message)