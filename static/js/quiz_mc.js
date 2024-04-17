function addContent() {
    event.preventDefault();

    // Disable the submit button
    $("#submit-button").prop("disabled", true);
    // Disable all radio buttons
    $('input[name="answer"]').prop("disabled", true);

    // Clear previous feedback
    $("#feedback").empty();

    let selectedOption = $('input[name="answer"]:checked').val(); // Get selected option

    let correctAnswer = $('#correct-answer').val();
    let questionId = question.id; // Access question ID directly from the question object

    // Compare selected option with correct answer
    if (selectedOption === correctAnswer) {
        $("#feedback").append('<p class="text-success">Correct!</p>');
    } else {
        // Display the correct option text
        $("#feedback").append('<p class="text-danger">Incorrect. The correct answer is: ' + correctAnswer + ')</p>');
    }

    console.log('Selected option:', selectedOption);

    $.ajax({
        type: "POST",
        url: "/submit-answer/" + questionId,
        data: {
            questionId: questionId, // Pass the question ID from the question object
            selectedOption: selectedOption,
            correctAnswer: correctAnswer
        },
        success: function(response) {
            console.log(response); // Log the response from the server
        },
        error: function(xhr, status, error) {
            console.error(error); // Log any errors
        }
    });
}

$(document).ready(function () {
    $("#submit-button").click(addContent);
});
