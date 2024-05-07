from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect
import json
app = Flask(__name__)

#data
user_data = {
    "lessons": {
        "intro": {
            "completed": False,
            "hovered_1": False,
            "hovered_2": False,
            "hovered_3": False,
            "hovered_4": False,
            "time_spent": 0,
        },
        "1": {
            "completed": False,
            "time_spent": 0
        },
        "2": {
            "completed": False,
            "time_spent": 0
        },
        "3": {
            "completed": False,
            "time_spent": 0
        },
        "4": {
            "completed": False,
            "time_spent": 0
        },
        "review": {
            "completed": False,
            "time_spent": 0
        },
    },
    "quiz": {
        "completed": False,
        "score": 0,
        "answers": {
            1: {"selected_option": None, "answer_correct": False, "answered": False},
            2: {"selected_option": None, "answer_correct": False, "answered": False},
            3: {"selected_option": None, "answer_correct": False, "answered": False},
            4: {"selected_option": None, "answer_correct": False, "answered": False},
            5: {"selected_option": None, "answer_correct": False, "answered": False},
            6: {"selected_option": None, "answer_correct": False, "answered": False},
            7: {"selected_option": None, "answer_correct": False, "answered": False},
            8: {"selected_option": None, "answer_correct": False, "answered": False},
        },
    }
}

legend = [
    {
        "name": "Foam",
        "image": "./media/legend/foam.png"
    },
    {
        "name": "Steamed Milk",
        "image": "./media/legend/milk.png"
    },
    {
        "name": "Cocoa",
        "image": "./media/legend/cocoa.png"
    },
    {
        "name": "Syrup",
        "image": "./media/legend/syrup.png"
    },
    {
        "name": "Water",
        "image": "./media/legend/water.png"
    },
    {
        "name": "Espresso",
        "image": "./media/legend/espresso.png"
    },
]

ingredients = [
    {
        "foam": {
            "name": "Foam",
            "image": "./media/legend/foam.png"
        },
        "foam2": {
            "name": "Foam",
            "image": "./media/legend/foam2.png"
        },
        "milk": {
            "name": "Steamed Milk",
            "image": "./media/legend/milk.png"
        },
        "cocoa": {
            "name": "Cocoa",
            "image": "./media/legend/cocoa.png"
        },
        "syrup": {
            "name": "Syrup",
            "image": "./media/legend/syrup.png"
        },
        "water": {
            "name": "Water",
            "image": "./media/legend/water.png"
        },
        "espresso": {
            "name": "Espresso",
            "image": "./media/legend/espresso.png"
        },
    }
]

home_data = {
    "title": "<span class='highlight'>Learn How To</span> Distinguish Coffee Drinks",
    "buttons": [
        {
            "text": "Start Learning",
            "link": "/learn/intro",
        },
        {
            "text": "Quiz Yourself",
            "link": "/quiz/1",
            "color": "white",
        }
    ]
}

quiz_review_data = {
    "buttons": [
        {
            "text": "Review Lessons",
            "link": "/learn/intro",
        },
        {
            "text": "Retake Quiz",
            "link": "/quiz/1",
            "color": "white",
        }
    ]
}

lesson_metadata = {
 "contents": {
        "1": "1. Black (Espresso)",
        "2": "2. Espresso + Steamed Milk",
        "3": "3. Espresso + Steamed Milk + Foam",
        "4": "4. Espresso + Others",
        "review": "Review",
        "quiz": "Quiz"
 }   
}

quiz_metadata = {
    "questions": {
        1: "Question 1: Select the image that corresponds to a Latte.",
        2: "Question 2: Select the final product.",
        3: "Question 3: Drag and drop the ingredients to make an Espresso.",
        4: "Question 4: Drag and drop the ingredients to make a Cortado.",
        5: "Question 5: Drag and drop the ingredients to make a Macchiato.",
        6: "Question 6: Drag and drop the ingredients to make a (Syrup) Latte.",
        7: "Question 7: Drag and drop the ingredients to make a Cappuccino.",
        8: "Question 8: Drag and drop the ingredients to make a Mocha.",
        "review": "Review"
    }
}

lessons = {
    "intro": {
      "id": "intro",
      "title": "Lesson Overview",
      "subtitle": "4 Categories",
      "contents": [
            {
                "categories": {
                    "title": "1. Black (Espresso)",
                    "drinks": [
                        {
                            "name": "Espresso",
                            "ingredients": [
                                ("espresso", 1)
                            ]
                        },
                        {
                            "name": "Americano",
                            "ingredients": [
                                ("espresso", 2),
                                ("water", 2)
                            ]
                        }
                    ]
                }
            },
            {
                "categories": {
                    "title": "2. Espresso + Steamed Milk",
                    "drinks": [
                        {
                            "name": "Macchiato",
                            "ingredients": [
                                ("espresso", 2),
                                ("milk", 1)
                            ]
                        },
                        {
                            "name": "Cortado",
                            "ingredients": [
                                ("espresso", 2),
                                ("milk", 2)
                            ]
                        }
                    ]
                }
            },
            {
                "categories": {
                    "title": "3. Espresso + Steamed Milk + Foam",
                    "drinks": [
                        {
                            "name": "Cappuccino",
                            "ingredients": [
                                ("espresso", 2),
                                ("milk", 2),
                                ("foam", 2)
                            ]
                        },
                        {
                            "name": "Latte",
                            "ingredients": [
                                ("espresso", 2),
                                ("milk", 3),
                                ("foam", 1)
                            ]
                        }
                    ]
                }
            },
            {
                "categories": {
                    "title": "4. Espresso + Others",
                    "drinks": [
                        {
                            "name": "Mocha",
                            "ingredients": [
                                ("espresso", 2),
                                ("cocoa", 1),
                                ("milk", 3),
                                ("foam", 1)
                            ]
                        },
                        {
                            "name": "Latte",
                            "ingredients": [
                                ("espresso", 2),
                                ("syrup", 1),
                                ("milk", 3),
                                ("foam", 1)
                            ]
                        }
                    ]
                }
            }
        ],
        "next": 1,
        "previous": "home"
    },
    "1": {
        "id": 1,
        "name": "1. Black (Espresso)",
        "video": "https://www.youtube.com/embed/LiNjMyAGVt0?si=_TVqL4wgbh8VpWZh",
        "video_start": 14,
        "video_end": 61,
        "video_header": "How to pull an espresso shot",
        "content_header": "Click on each drink to learn how to make it",
        "drinks": [
            {
                "drink_id": 1,
                "slides": [
                    {
                        "slide_id": 1,
                        "body": "Espresso",
                        "body_type": "text",
                    },
                    {
                        "slide_id": 2,
                        "title": "Pull espresso shots",
                        "title_type": "text",
                        "body": "./media/learning/espresso.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 3,
                        "title": "Reset",
                        "title_type": "button",
                        "body": [
                            ("espresso", 1)
                        ],
                        "body_type": "drink",
                        "footer": "Espresso",
                        "footer_type": "text"
                    }
                ]
            },
            {
                "drink_id": 2,
                "slides": [
                    {
                        "slide_id": 1,
                        "body": "Americano",
                        "body_type": "text",
                    },
                    {
                        "slide_id": 2,
                        "title": "Pull espresso shots",
                        "title_type": "text",
                        "body": "./media/learning/espresso.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 3,
                        "title": "Dilute with water",
                        "title_type": "text",
                        "body": "./media/learning/water.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 4,
                        "title": "Reset",
                        "title_type": "button",
                        "body": [
                            ("espresso", 2),
                            ("water", 2)
                        ],
                        "body_type": "drink",
                        "footer": "Americano",
                        "footer_type": "text"
                    }
                ]
            }
        ],
        "next": 2,
        "previous": "intro"
    },
    "2": {
        "id": 2,
        "name": "2. Espresso + Steamed Milk",
        "video": "https://www.youtube.com/embed/OtdlZbc9XK0?si=QlPPzFceUqSZ5txQ",
        "video_start": 0,
        "video_end": 81,
        "video_header": "How to steam milk",
        "content_header": "Click on each drink to learn how to make it",
        "drinks": [
            {
                "drink_id": 1,
                "slides": [
                    {
                        "slide_id": 1,
                        "body": "Macchiato",
                        "body_type": "text",
                    },
                    {
                        "slide_id": 2,
                        "title": "Pull espresso shots",
                        "title_type": "text",
                        "body": "./media/learning/espresso.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 3,
                        "title": "Splash of milk",
                        "title_type": "text",
                        "body": "./media/learning/milk.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 4,
                        "title": "Reset",
                        "title_type": "button",
                        "body": [
                            ("espresso", 2),
                            ("milk", 1)
                        ],
                        "body_type": "drink",
                        "footer": "Espresso",
                        "footer_type": "text"
                    }
                ]
            },
            {
                "drink_id": 2,
                "slides": [
                    {
                        "slide_id": 1,
                        "body": "Cortado",
                        "body_type": "text",
                    },
                    {
                        "slide_id": 2,
                        "title": "Pull espresso shots",
                        "title_type": "text",
                        "body": "./media/learning/espresso.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 3,
                        "title": "Equal part milk",
                        "title_type": "text",
                        "body": "./media/learning/milk.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 4,
                        "title": "Reset",
                        "title_type": "button",
                        "body": [
                            ("espresso", 2),
                            ("milk", 2)
                        ],
                        "body_type": "drink",
                        "footer": "Americano",
                        "footer_type": "text"
                    }
                ]
            }
        ],
        "next": 3,
        "previous": 1
    },
    "3": {
        "id": 3,
        "name": "3. Espresso + Steamed Milk + Foam",
        "video": "https://www.youtube.com/embed/NLO0mWJuIHk?si=IwSFV4c-V2i1-Gtw",
        "video_start": 0,
        "video_end": 85,
        "video_header": "How to make foam",
        "content_header": "Click on each drink to learn how to make it",
        "drinks": [
            {
                "drink_id": 1,
                "slides": [
                    {
                        "slide_id": 1,
                        "body": "Cappuccino",
                        "body_type": "text",
                    },
                    {
                        "slide_id": 2,
                        "title": "Pull espresso shots",
                        "title_type": "text",
                        "body": "./media/learning/espresso.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 3,
                        "title": "Equal part milk",
                        "title_type": "text",
                        "body": "./media/learning/milk.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 4,
                        "title": "Equal part foam",
                        "title_type": "text",
                        "body": "./media/learning/foam.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 5,
                        "title": "Reset",
                        "title_type": "button",
                        "body": [
                            ("espresso", 2),
                            ("milk", 2),
                            ("foam", 2)
                        ],
                        "body_type": "drink",
                        "footer": "Espresso",
                        "footer_type": "text"
                    }
                ]
            },
            {
                "drink_id": 2,
                "slides": [
                    {
                        "slide_id": 1,
                        "body": "Latte",
                        "body_type": "text",
                    },
                    {
                        "slide_id": 2,
                        "title": "Pull espresso shots",
                        "title_type": "text",
                        "body": "./media/learning/espresso.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 3,
                        "title": "More milk",
                        "title_type": "text",
                        "body": "./media/learning/milk.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 4,
                        "title": "Less foam",
                        "title_type": "text",
                        "body": "./media/learning/foam.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 5,
                        "title": "Reset",
                        "title_type": "button",
                        "body": [
                            ("espresso", 2),
                            ("milk", 3),
                            ("foam", 1)
                        ],
                        "body_type": "drink",
                        "footer": "Americano",
                        "footer_type": "text"
                    }
                ]
            }
        ],
        "next": 4,
        "previous": 2,
    },
    "4": {
        "id": 4,
        "name": "4. Espresso + Others",
        "video": "https://www.youtube.com/embed/8FLzhL-T25E?si=v6iX685mOVF64UWp",
        "video_start": 18,
        "video_end": 87,
        "video_header": "How to add flavor",
        "content_header": "Click on each drink to learn how to make it",
        "drinks": [
            {
                "drink_id": 1,
                "slides": [
                    {
                        "slide_id": 1,
                        "body": "Mocha",
                        "body_type": "text",
                    },
                    {
                        "slide_id": 2,
                        "title": "Pull espresso shots",
                        "title_type": "text",
                        "body": "./media/learning/espresso.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 3,
                        "title": "Cocoa powder",
                        "title_type": "text",
                        "body": "./media/learning/cocoa.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 4,
                        "title": "Milk like latte (more milk)",
                        "title_type": "text",
                        "body": "./media/learning/milk.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 5,
                        "title": "Foam like latte (less foam)",
                        "title_type": "text",
                        "body": "./media/learning/foam.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 6,
                        "title": "Reset",
                        "title_type": "button",
                        "body": [
                            ("espresso", 2),
                            ("cocoa", 1),
                            ("milk", 3),
                            ("foam", 1)
                        ],
                        "body_type": "drink",
                        "footer": "Espresso",
                        "footer_type": "text"
                    }
                ]
            },
            {
                "drink_id": 2,
                "slides": [
                    {
                        "slide_id": 1,
                        "body": "(Syrup) Latte",
                        "body_type": "text",
                    },
                    {
                        "slide_id": 2,
                        "title": "Pull espresso shots",
                        "title_type": "text",
                        "body": "./media/learning/espresso.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 3,
                        "title": "Syrup",
                        "title_type": "text",
                        "body": "./media/learning/syrup.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 4,
                        "title": "Milk like latte (more milk)",
                        "title_type": "text",
                        "body": "./media/learning/milk.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 5,
                        "title": "Foam like latte (less foam)",
                        "title_type": "text",
                        "body": "./media/learning/foam.png",
                        "body_type": "image",
                    },
                    {
                        "slide_id": 6,
                        "title": "Reset",
                        "title_type": "button",
                        "body": [
                            ("espresso", 2),
                            ("syrup", 1),
                            ("milk", 3),
                            ("foam", 1)
                        ],
                        "body_type": "drink",
                        "footer": "Espresso",
                        "footer_type": "text"
                    }
                ]
            }
        ],
        "next": "review",
        "previous": 3,
    },
    "review": {
        "id": "review",
        "name": "REVIEW",
        "contents": [
            {
                "categories": {
                    "title": "1. Black (Espresso)",
                    "notes": [
                        "",
                        "Americano is a diluted espresso",
                    ],
                    "drinks": [
                        {
                            "name": "Espresso",
                            "ingredients": [
                                ("espresso", 1)
                            ]
                        },
                        {
                            "name": "Americano",
                            "ingredients": [
                                ("espresso", 2),
                                ("water", 2)
                            ]
                        }
                    ]
                }
            },
            {
                "categories": {
                    "title": "2. Espresso + Steamed Milk",
                    "notes": [
                        "Macchiato has a splash of milk",
                        "Cortado has equal parts milk (1:1 ratio)",
                    ],
                    "drinks": [
                        {
                            "name": "Macchiato",
                            "ingredients": [
                                ("espresso", 2),
                                ("milk", 1)
                            ]
                        },
                        {
                            "name": "Cortado",
                            "ingredients": [
                                ("espresso", 2),
                                ("milk", 2)
                            ]
                        }
                    ]
                }
            },
            {
                "categories": {
                    "title": "3. Espresso + Steamed Milk + Foam",
                    "notes": [
                        "Cappuccino is equal parts espresso, milk, and foam (1:1:1 ratio)",
                        "Latte is more milk and less foam",
                    ],
                    "drinks": [
                        {
                            "name": "Cappuccino",
                            "ingredients": [
                                ("espresso", 2),
                                ("milk", 2),
                                ("foam", 2)
                            ]
                        },
                        {
                            "name": "Latte",
                            "ingredients": [
                                ("espresso", 2),
                                ("milk", 3),
                                ("foam", 1)
                            ]
                        }
                    ]
                }
            },
            {
                "categories": {
                    "title": "4. Espresso + Others",
                    "notes": [
                        "Mocha is a latte with chocolate",
                        "(Syrup) latte is a latte with different flavors",
                    ],
                    "drinks": [
                        {
                            "name": "Mocha",
                            "ingredients": [
                                ("espresso", 2),
                                ("cocoa", 1),
                                ("milk", 3),
                                ("foam", 1)
                            ]
                        },
                        {
                            "name": "(Syrup) Latte",
                            "ingredients": [
                                ("espresso", 2),
                                ("syrup", 1),
                                ("milk", 3),
                                ("foam", 1)
                            ]
                        }
                    ]
                }
            }
        ],
        "next": "quiz",
        "previous": 4
    }
}

lesson_quiz = {
    "2": {
        "question": "What is the ratio of espresso to steamed milk in a cortado?",
        "options": [
            {"id": 1, "text": "1:1"},
            {"id": 2, "text": "1:2"},
            {"id": 3, "text": "1:3"},
            {"id": 4, "text": "1:4"},
            {"id": 5, "text": "1:5"}
        ],
        "correct_answer": 1,
    },
    "4": {
        "question": "What goes in a mocha?",
        "options": [
            {"id": 1, "text": "Espresso"},
            {"id": 2, "text": "Espresso + water"},
            {"id": 3, "text": "Espresso + steamed milk"},
            {"id": 4, "text": "Espresso + steamed milk + foam"},
            {"id": 5, "text": "Espresso + steamed milk + foam + chocolate"}
        ],
        "correct_answer": 5,
    },
}

quiz = {
    "id": "quiz",
    "name": "Quiz",
    "questions": [
    {
        "id": 1,
        "question": "Select the image that corresponds to a Latte.",
        "question_type": "drink_selection",
        "options": [
            {"id": 1, "text": "Espresso",
                "ingredients": [
                    ("espresso", 1)
                ]
            },
            {"id": 2, "text": "Latte",
                            "ingredients": [
                                ("espresso", 2),
                                ("milk", 3),
                                ("foam", 1)
                            ]},
            {"id": 3, "text": "Cappuccino", "ingredients": [
                                ("espresso", 2),
                                ("milk", 2),
                                ("foam", 2)
                            ]},
            {"id": 4, "text": "Americano", "ingredients": [
                                ("espresso", 2),
                                ("water", 2)
                            ]}
        ],
        "correct_answer": 2,
        "next": 2,
    },
    {
        "id": 2,
        "question": "Select the final product.",
        "question_img": "/media/quiz/4_question.png",
        "question_type": "drink_selection",
        "options": [
            {"id": 1, "text": "Mocha", "ingredients": [
                                ("espresso", 2),
                                ("cocoa", 1),
                                ("milk", 3),
                                ("foam", 1)
                            ]},
            {"id": 2, "text": "Cappuccino", "ingredients": [
                                ("espresso", 2),
                                ("milk", 2),
                                ("foam", 2)
                            ]},
            {"id": 3, "text": "Macchiato",  "ingredients": [
                                ("espresso", 2),
                                ("milk", 1)
                            ]},
            {"id": 4, "text": "Americano",  "ingredients": [
                                ("espresso", 2),
                                ("water", 2)
                            ]}
        ],
        "correct_answer": 4,
        "next": 3,
        "previous": 1
    },
    {
        "id": 3,
        "question": "Drag and drop the ingredients to make an ",
        "text": "Espresso",
        "correct_answer": [
            ("espresso", 1)
        ],
        "next": 4,
        "previous": 2
    },
    {
        "question": "Drag and drop the ingredients to make a ",
        "text": "Cortado",
        "correct_answer": [
            ("espresso", 2),
            ("milk", 2)
        ],
        "id": 4,
        "next": 5,
        "previous": 3
    },
    {
        "question": "Drag and drop the ingredients to make a ",
        "text": "Macchiato",
        "correct_answer": [
            ("espresso", 2),
            ("milk", 1)
        ],
        "id": 5,
        "next": 6,
        "previous": 4
    },
    {
        "question": "Drag and drop the ingredients to make a ",
        "text": "(Syrup) Latte",
        "correct_answer": [
            ("espresso", 2),
            ("syrup", 1),
            ("milk", 3),
            ("foam", 1)
        ],
        "id": 6,
        "next": 7,
        "previous": 5
    },
    {
        "question": "Drag and drop the ingredients to make a ",
        "text": "Cappuccino",
        "correct_answer": [
            ("espresso", 2),
            ("milk", 2),
            ("foam", 2)
        ],
        "id": 7,
        "next": 8,
        "previous": 6
    },
    {
        "question": "Drag and drop the ingredients to make a ",
        "text": "Mocha",
        "correct_answer": [
            ("espresso", 2),
            ("cocoa", 1),
            ("milk", 3),
            ("foam", 1)
        ],
        "id": 8,
        "next": 9,
        "previous": 7
    }
    ]
}


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html", data = home_data)

@app.route('/learn/<page_number>/', methods=['GET'])
def learn(page_number):
    if page_number == "intro":
        # Render the intro page
        intro_data = lessons.get("intro")
        if intro_data:
            return render_template("intro.html", lesson=intro_data, lesson_metadata=lesson_metadata, legend=legend, ingredients=ingredients)
        else:
            return "Intro data not found", 404
    elif page_number == "review":
        # Render the review page
        review_data = lessons.get("review")
        if review_data:
            return render_template("review.html", lesson=review_data, lesson_metadata=lesson_metadata, legend=legend, ingredients=ingredients)
        else:
            return "Review data not found", 404
    else:
        # Render other lesson pages
        lesson_data = lessons.get(page_number)
        if lesson_data:
            return render_template("lesson.html", lesson=lesson_data, lesson_metadata=lesson_metadata, legend=legend, ingredients=ingredients, completed=user_data["lessons"][page_number]["completed"])
        else:
            return "Lesson data not found", 404

@app.route('/learn/update/<page_number>/', methods=['POST'])
def update_lesson(page_number):
    user_data["lessons"][page_number] = request.json
    return jsonify(user_data["lessons"][page_number])

@app.route('/quiz/<int:question_id>', methods=['GET'])
def quiz_question(question_id):
    if question_id == 1:
        # Reset the quiz score to 0
        user_data["quiz"]["score"] = 0
        
        # Reset all answers and their attributes
        user_data["quiz"] = {
            "completed": False,
            "score": 0,
            "answers": {
                1: {"selected_option": None, "answer_correct": False, "answered": False},
                2: {"selected_option": None, "answer_correct": False, "answered": False},
                3: {"selected_option": None, "answer_correct": False, "answered": False},
                4: {"selected_option": None, "answer_correct": False, "answered": False},
                5: {"selected_option": None, "answer_correct": False, "answered": False},
                6: {"selected_option": None, "answer_correct": False, "answered": False},
                7: {"selected_option": None, "answer_correct": False, "answered": False},
                8: {"selected_option": None, "answer_correct": False, "answered": False},
            },
        }
    if(question_id == 9):
        return redirect('/quiz/review')
    print(question_id, quiz["questions"][question_id - 1])
    question_data = quiz["questions"][question_id - 1]
    question_metadata = quiz_metadata["questions"]

    if question_id in [1, 2]:
        template_name = "quiz_mc_img.html"
    elif question_id in [3,4,5,6,7,8]:
        template_name = "quiz_drag.html"
    else:
        return redirect('/quiz/review')
    
    if question_data.get("next") == "Review":
        # Redirect to the review page
        return redirect('/quiz/review')

    return render_template(template_name, question=question_data, metadata=question_metadata, legend=legend, ingredients=ingredients)

@app.route('/submit-answer/<int:question_id>', methods=['POST'])
def submit_answer(question_id):
    selected_option = request.form.get('selectedOption')
    correct_answer = request.form.get('correctAnswer')
    
    answer_correct = selected_option == correct_answer
    

    user_data["quiz"]["answers"][question_id] = {
        "selected_option": selected_option,
        "answer_correct": answer_correct,
        "answered": True
    }
    
    if answer_correct:
        user_data["quiz"]["score"] += 1
    print(user_data["quiz"]["score"])
    print(f'Question {question_id}: Selected option: {selected_option}, Answer correct: {answer_correct}')

    return jsonify(correct=answer_correct)

@app.route('/quiz/review')
def quiz_review():
    # Pass user_data to the template for rendering
    return render_template('quiz_review.html', user_data=user_data, quiz=quiz, quiz_review_data=quiz_review_data)

@app.route('/get-category-drinks', methods=['GET'])
def get_category_drinks():
    title = request.args.get('title')
    for category in lessons['intro']['contents']:
        if category['categories']['title'] == title:
            return jsonify(drinks=category['categories']['drinks'])
    return jsonify(error='Category not found'), 404


if __name__ == '__main__':
    app.run(debug=True)