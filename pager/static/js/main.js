$(document).ready(function () {

    var table = $('#main_table').DataTable({
        responsive: true,
        "lengthMenu": [[5, 10, 25, 50, -1], [5, 10, 25, 50, "All"]]
    });

    $("#scrollBtn").click(function () {
        $('html,body').animate({
            scrollTop: $("#table_container").offset().top
        },
            'slow');
    });

    // new $.fn.dataTable.FixedHeader(table);
    var noteTextarea = $('#note-textarea');
    var instructions = $('#recording-instructions');
    var notesList = $('ul#notes');

    var noteContent = '';

    try {
        var SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        var recognition = new SpeechRecognition();


        recognition.continuous = true;

        recognition.onresult = function (event) {
            var current = event.resultIndex;
            // Get a transcript of what was said.
            var transcript = event.results[current][0].transcript;
            var mobileRepeatBug = (current == 1 && transcript == event.results[0][0].transcript);

            if (!mobileRepeatBug) {
                noteContent += transcript;
                noteTextarea.val(noteContent);
            }
        };

        recognition.onstart = function () {
            instructions.text('Voice recognition activated. Try speaking into the microphone.');
        }

        recognition.onspeechend = function () {
            instructions.text('You were quiet for a while so voice recognition turned itself off.');
        }

        recognition.onerror = function (event) {
            if (event.error == 'no-speech') {
                instructions.text('No speech was detected. Try again.');
            };
        }
    }
    catch (e) {
        console.error(e);
    }

    /*-----------------------------
          App buttons and input 
    ------------------------------*/

    $('#start-record-btn').on('click', function (e) {
        if (noteContent.length) {
            noteContent += ' ';
        }
        recognition.start();
    });


    $('#pause-record-btn').on('click', function (e) {
        recognition.stop();
        instructions.text('Voice recognition paused.');
    });

    // Sync the text inside the text area with the noteContent variable.
    noteTextarea.on('input', function () {
        noteContent = $(this).val();
    })

    $('#save-note-btn').on('click', function (e) {
        try { recognition.stop(); }
        catch (e) {
            console.log(e);
        }

        if (!noteContent.length) {
            instructions.text('Could not save empty note. Please add a message to your note.');
        }
        else {
            postToDjango(noteContent);
            readOutLoud(noteContent);
        }

    })


    /*-----------------------------
          Speech Synthesis 
    ------------------------------*/
    var dropdown_val = "hi-EN"

    $(".voice_select").change(function () {
        dropdown_val = $(".voice_select").val();
    });

    function readOutLoud(message) {
        var speech = new SpeechSynthesisUtterance();

        speech.text = message;
        speech.volume = 1;
        speech.rate = 1;
        speech.pitch = 1;
        speech.lang = dropdown_val;

        window.speechSynthesis.speak(speech);
    }



    /*-----------------------------
          Helper Functions 
    ------------------------------*/

    function postToDjango(textData) {
        $.ajax({
            type: "GET",
            url: "/savetextaudio/",
            data: {
                "text": textData,
                "language": dropdown_val,
            },
            success: function (data) {
                console.log("success");
                console.log(data);
                // $('#main_table').DataTable();
                location.reload();
            },
            failure: function (data) {
                console.log("failure");
                console.log(data);
            },
        });
    }
})