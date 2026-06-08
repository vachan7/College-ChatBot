def get_response(user_input):

    user_input = user_input.lower()

    responses = {
        "college timing":
            "College timings are 9 AM to 4 PM.",

        "library":
            "The library is open from 8 AM to 6 PM.",

        "hostel":
            "Hostel applications can be submitted through the administration office.",

        "fees":
            "Fees can be paid online through the student portal.",

        "courses":
            "We offer CSE, ECE, Mechanical, Civil and MBA programs.",

        "principal":
            "The principal's office is located in the administration block.",
        "hi":
            "hello how can i assist you?"
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I don't understand that question."