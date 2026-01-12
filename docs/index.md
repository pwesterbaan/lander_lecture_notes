<h1>Dr. Westerbaan's Lecture Notes</h1>

Below are links to notes used at Lander University:

<ul>
  <h1> math121 </h1>
  <li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math121Notes.pdf" target="_blank">math121Notes.pdf</a></li>
  <details name="annotated_notes" id="math121_NoteKeys">
    <summary>math121 Annotated Notes</summary>
  </details><br>

  <h1> math123 </h1>
  <li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math123Notes.pdf" target="_blank">math123Notes.pdf</a></li>
  <details name="annotated_notes" id="math123_NoteKeys">
    <summary>math123 Annotated Notes</summary>
  </details><br>

  <h1> math125 </h1>
  <li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math125Notes.pdf" target="_blank">math125Notes.pdf</a></li>
  <details name="annotated_notes" id="math125_NoteKeys">
    <summary>math125 Annotated Notes</summary>
  </details><br>

  <h1> math211 </h1>
  <li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math211Notes.pdf" target="_blank">math211Notes.pdf</a></li>
  <details name="annotated_notes" id="math211_NoteKeys">
    <summary>math211 Annotated Notes</summary>
  </details><br>
</ul>

<span style="float:right">Last Modified: 2026-01-12 15:13</span>

<script>
    // For anyone looking at this:
    // Obviously this is not a secure way to hide links
    // I'm hiding these links to encourage my students
    // to actually take notes and pay attention during class
    function show_links_by_date(noteKeysDir,dateUrlArray){
        baseURL="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/";
        annNotesDir=noteKeysDir+"/annotated_notes/";

        var list = document.createElement('ul');      // Create the list element

        dateUrlArray.forEach(element => {
          [dispDate, fileName]=element;
          if (new Date() >= new Date(dispDate)){

            var myLink=document.createElement('a');   // Create the link
            myLink.href = new URL(fileName,baseURL+annNotesDir);
            myLink.text = fileName;
            myLink.target = "_blank"

            var item = document.createElement('li');  // Create a list item
            item.appendChild(myLink);                 // Add the link to it
            list.appendChild(item);                   // Add item to the list
          }
        });
    document.getElementById(noteKeysDir).appendChild(list);
    }

  var releaseDatesList=[
      ["2026-01-14T14:00:00","mathApp_harshbarger_1p1_annotated.pdf"],
      ["2026-01-21T14:00:00","mathApp_harshbarger_1p3_annotated.pdf"],
      ["2026-01-23T14:00:00","mathApp_harshbarger_1p4_annotated.pdf"],
      ["2026-01-27T14:00:00","mathApp_harshbarger_1p5_annotated.pdf"],
      ["2026-01-30T14:00:00","mathApp_harshbarger_1p6_annotated.pdf"],
      ["2026-02-11T14:00:00","mathApp_harshbarger_4p1_annotated.pdf"],
      ["2026-02-17T14:00:00","mathApp_harshbarger_4p2_annotated.pdf"],
      ["2026-02-24T14:00:00","mathApp_harshbarger_5p1_annotated.pdf"],
      ["2026-03-10T14:00:00","mathApp_harshbarger_5p2_annotated.pdf"],
      ["2026-03-11T14:00:00","mathApp_harshbarger_5p3_annotated.pdf"],
      ["2026-03-19T14:00:00","mathApp_harshbarger_6p1_annotated.pdf"],
      ["2026-03-24T14:00:00","mathApp_harshbarger_6p2_annotated.pdf"],
      ["2026-03-31T14:00:00","mathApp_harshbarger_6p3_annotated.pdf"],
      ["2026-04-01T14:00:00","mathApp_harshbarger_6p5_annotated.pdf"],
      ["2026-04-16T14:00:00","mathApp_harshbarger_2p1_annotated.pdf"],
      ["2026-04-16T14:00:00","mathApp_harshbarger_2p2_annotated.pdf"],
      ["2026-04-22T14:00:00","mathApp_harshbarger_2p3_annotated.pdf"],
      ["3000-01-01T13:00:00","mathApp_harshbarger_6p4_annotated.pdf"],
      ]
  show_links_by_date("math121_NoteKeys",releaseDatesList);

  var releaseDatesList=[
      ["2026-01-14T09:00:00","math123Notes_1p4_annotated.pdf"],
      ["2026-01-16T09:00:00","math123Notes_2p1_annotated.pdf"],
      ["2026-01-21T09:00:00","math123Notes_2p2_annotated.pdf"],
      ["2026-01-28T09:00:00","math123Notes_2p4_annotated.pdf"],
      ["2026-02-02T09:00:00","math123Notes_2p5_annotated.pdf"],
      ["2026-02-06T09:00:00","math123Notes_2p6_annotated.pdf"],
      ["2026-02-16T09:00:00","math123Notes_3p1_annotated.pdf"],
      ["2026-02-18T09:00:00","math123Notes_3p2_annotated.pdf"],
      ["2026-02-23T09:00:00","math123Notes_3p3_annotated.pdf"],
      ["2026-02-25T09:00:00","math123Notes_3p5_annotated.pdf"],
      ["2026-03-11T09:00:00","math123Notes_3p6_annotated.pdf"],
      ["2026-03-23T09:00:00","math123Notes_4p1_annotated.pdf"],
      ["2026-03-27T09:00:00","math123Notes_4p2_annotated.pdf"],
      ["2026-03-30T09:00:00","math123Notes_4p4_annotated.pdf"],
      ["2026-04-03T09:00:00","math123Notes_4p5_annotated.pdf"],
      ["2026-04-06T09:00:00","math123Notes_5p4_annotated.pdf"],
      ["2026-04-10T09:00:00","math123Notes_5p5_annotated.pdf"],
      ["2026-04-13T09:00:00","math123Notes_5p6_annotated.pdf"],
      ["2026-04-20T09:00:00","math123Notes_6p1_annotated.pdf"],
      ["2026-04-22T09:00:00","math123Notes_6p2_annotated.pdf"],
      ["2026-04-24T09:00:00","math123Notes_6p5_annotated.pdf"],
      ]
  show_links_by_date("math123_NoteKeys",releaseDatesList);

  var releaseDatesList=[
      ["2026-01-14T12:00:00","discMathEpp5_01p1_annotated.pdf"],
      ["2026-01-16T12:00:00","discMathEpp5_01p2_annotated.pdf"],
      ]
  show_links_by_date("math125_NoteKeys",releaseDatesList);

  var releaseDatesList=[
      ["2026-01-13T11:00:00","math211Notes_1p1_annotated.pdf"],
      ["2026-01-15T11:00:00","math211Notes_1p2_1p4_1p5_annotated.pdf"],
      ["2026-01-22T11:00:00","math211Notes_2p1_2p2_2p3_annotated.pdf"],
      ["2026-01-22T11:00:00","math211Notes_2p4_2p5_annotated.pdf"],
      ["2026-01-29T11:00:00","math211Notes_3p1_annotated.pdf"],
      ["2026-02-03T11:00:00","math211Notes_3p2_3p3_annotated.pdf"],
      ["2026-02-05T11:00:00","math211Notes_3p4_3p5_annotated.pdf"],
      ["2026-02-17T11:00:00","math211Notes_4p1_4p2_annotated.pdf"],
      ["2026-02-19T11:00:00","math211Notes_4p3_4p4_annotated.pdf"],
      ["2026-02-26T11:00:00","math211Notes_6p1_6p2_annotated.pdf"],
      ["2026-03-10T11:00:00","math211Notes_7p1_7p2_7p3_annotated.pdf"],
      ["2026-03-26T11:00:00","math211Notes_7p4_8p1_8p2_annotated.pdf"],
      ["2026-03-31T11:00:00","math211Notes_8p3_9p1_9p2_annotated.pdf"],
      ["2026-04-02T11:00:00","math211Notes_9p3_annotated.pdf"],
      ["2026-04-07T11:00:00","math211Notes_9p4_annotated.pdf"],
      ]
  show_links_by_date("math211_NoteKeys",releaseDatesList);
</script>