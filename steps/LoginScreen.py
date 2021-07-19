from behave import given, when, then

@given("Launch the App and Click on Login Button")
def methodOne(context):
    print("L1 - Launching the App")


@when("click on Login Button")
def methodTwo(context):
    print("Botao clicado")


@when("Enter {emailid} UserID")
def method(context, emailid):
    print("L2 - Enter the UserID in Login Screen {}".format(emailid))


@then("Verify Home Screen")
def methodThree(context):
    print("Verify Home Screen")

