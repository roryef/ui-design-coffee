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
            "clicked_1": False,
            "clicked_2": False,
            "clicked_3": False,
            "clicked_4": False,
        },
        "1": {
            "completed": False,
            "clicked_1": False,
            "clicked_2": False,
            "watched_video": False,
            "time_spent": 0
        },
        "2": {
            "completed": False,
            "clicked_1": False,
            "clicked_2": False,
            "watched_video": False,
            "time_spent": 0
        },
        "3": {
            "completed": False,
            "clicked_1": False,
            "clicked_2": False,
            "watched_video": False,
            "time_spent": 0
        },
        "4": {
            "completed": False,
            "clicked_1": False,
            "clicked_2": False,
            "watched_video": False,
            "time_spent": 0
        },
        "review": {
            "completed": False,
            "time_spent": 0
        },
    }
}

legend = {
    [
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
}

ingredients = {
    {
        "foam": {
           "name": "Foam",
           "image": "./media/legend/foam.png" 
        },
        "milk": {
            "name": "Steamed Milk",
            "image": "./media/legend/milk.png"
        },
        "cocoa":{
            "name": "Cocoa",
            "image": "./media/legend/cocoa.png"
        },
        "syrup":{
            "name": "Syrup",
            "image": "./media/legend/syrup.png"  
        },
        "water":{
            "name": "Water",
            "image": "./media/legend/water.png"  
        },
        "espresso":{
            "name": "Espresso",
            "image": "./media/legend/espresso.png"  
        },
    }
}

home_data = {
    "title": "<span class='highlight'>Welcome!</span> You will learn how to <span class='highlight'>Distinguish Coffee</span> today!",
    "buttons": [
        {
            "text": "Learn",
            "link": "/learn/1",
        },
        {
            "text": "Quiz",
            "link": "/quiz/1",
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
lessons = {
    "intro": {
      "title": "The lesson will teach you 4 types of coffee drinks",
      "subtitle": "Click on each category to reveal the drinks",
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
        "video_header": "Click to watch how to pull an espresso",
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
        "video_header": "Click to watch how to steam milk",
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
        "video_header": "Click to watch how to make foam",
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
        "video_header": "Click to watch how to add flavor",
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
                        "American is a diluted espresso",
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
                        "Cortado is equal parts milk (1:1 ratio)",
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
                        "Cappuccino is equal parts espresso, milk and foam (1:1:1 ratio)",
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
                        "(Syrup) latte a latte with different flavors",
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
        "next": "quiz",
        "previous": 4
    }
}


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html", data = home_data)

@app.route('/learn/<page_number>', methods=['GET'])
def learn(page_number):
    return render_template("lesson.html", lesson=lessons[page_number], lesson_metadata=lesson_metadata, legend=legend, ingredients=ingredients)

@app.route('/learn/<page_number>/update', methods=['POST'])
def update_lesson(page_number):
    user_data["lessons"][page_number] = request.json
    return jsonify(user_data["lessons"][page_number])

if __name__ == '__main__':
    app.run(debug=True)