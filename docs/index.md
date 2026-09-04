---
layout: default
title: Westerbaan--Lander lecture notes
---

<h1>Dr. Westerbaan's Lecture Notes</h1>

Below are links to notes used at Lander University:

<ul>
  <h1> math114 </h1>
  <li>
    <a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math114Notes.pdf" target="_blank">math114Notes.pdf</a>
    <details name="annotated_notes" id="math114_NoteKeys">
      <summary>math114 Annotated Notes (Click to expand)</summary>
    </details>

  </li><br>
  <h1> math121 </h1>
  <li>
    <a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math121Notes.pdf" target="_blank">math121Notes.pdf</a>
    <details name="annotated_notes" id="math121_NoteKeys">
      <summary>math121 Annotated Notes (Click to expand)</summary>
    </details>

  </li><br>
  <h1> math123 </h1>
  <li>
    <a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math123Notes.pdf" target="_blank">math123Notes.pdf</a>
    <details name="annotated_notes" id="math123_NoteKeys">
      <summary>math123 Annotated Notes (Click to expand)</summary>
    </details>

  </li><br>
  <h1> math125 </h1>
  <li>
    <a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math125Notes.pdf" target="_blank">math125Notes.pdf</a>
    <details name="annotated_notes" id="math125_NoteKeys">
      <summary>math125 Annotated Notes (Click to expand)</summary>
    </details>

  </li><br>
  <h1> math211 </h1>
  <li>
    <a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math211Notes.pdf" target="_blank">math211Notes.pdf</a>
    <details name="annotated_notes" id="math211_NoteKeys">
      <summary>math211 Annotated Notes (Click to expand)</summary>
    </details>

  </li><br></ul>

<!---<a href="about_me">About me!</a>-->
<span style="float:right">Last Modified: 2026-09-04T10:28</span>

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
      ["2026-08-19T10:00:00","math114Notes_1p1_annotated.pdf"],
      ["2026-08-24T10:00:00","math114Notes_1p2_annotated.pdf"],
      ["2026-08-28T10:00:00","math114Notes_1p3_annotated.pdf"],
      ["2026-08-31T10:00:00","math114Notes_1p4_annotated.pdf"],
      ["2026-09-02T10:00:00","math114Notes_1p5_annotated.pdf"],
      ["2026-09-04T10:00:00","math114Notes_1p6_annotated.pdf"],
      ]
  show_links_by_date("math114_NoteKeys",releaseDatesList);

  var releaseDatesList=[
      ["2026-08-21T13:00:00","math121Notes_1p1_annotated.pdf"],
      ["2026-08-24T13:00:00","math121Notes_1p3_annotated.pdf"],
      ["2026-08-26T13:00:00","math121Notes_1p4_annotated.pdf"],
      ["2026-08-31T13:00:00","math121Notes_1p5_annotated.pdf"],
      ["2026-09-04T13:00:00","math121Notes_1p6_annotated.pdf"],
      ["2026-09-16T13:00:00","math121Notes_4p1_annotated.pdf"],
      ["2026-09-23T13:00:00","math121Notes_4p2_annotated.pdf"],
      ["2026-09-30T13:00:00","math121Notes_5p1_annotated.pdf"],
      ["2026-10-05T13:00:00","math121Notes_5p2_annotated.pdf"],
      ["2026-10-12T13:00:00","math121Notes_5p3_annotated.pdf"],
      ["2026-10-19T13:00:00","math121Notes_6p1_annotated.pdf"],
      ["2026-10-23T13:00:00","math121Notes_6p2_annotated.pdf"],
      ["2026-10-28T13:00:00","math121Notes_6p3_annotated.pdf"],
      ["2026-11-02T13:00:00","math121Notes_6p5_annotated.pdf"],
      ["2026-11-13T13:00:00","math121Notes_2p1_annotated.pdf"],
      ["2026-11-18T13:00:00","math121Notes_2p2_annotated.pdf"],
      ["2026-11-30T13:00:00","math121Notes_2p3_annotated.pdf"],
      ["3000-01-01T13:00:00","math121Notes_6p4_annotated.pdf"],
      ]
  show_links_by_date("math121_NoteKeys",releaseDatesList);

  var releaseDatesList=[
      ["2026-08-19T11:00:00","math123Notes_1p4_annotated.pdf"],
      ["2026-08-21T11:00:00","math123Notes_2p1_annotated.pdf"],
      ["2026-08-25T11:00:00","math123Notes_2p2_annotated.pdf"],
      ["2026-09-01T11:00:00","math123Notes_2p4_annotated.pdf"],
      ["2026-09-04T11:00:00","math123Notes_2p5_annotated.pdf"],
      ["2026-09-11T11:00:00","math123Notes_2p6_annotated.pdf"],
      ["2026-09-21T11:00:00","math123Notes_3p1_annotated.pdf"],
      ["2026-09-23T11:00:00","math123Notes_3p2_annotated.pdf"],
      ["2026-09-28T11:00:00","math123Notes_3p3_annotated.pdf"],
      ["2026-10-01T11:00:00","math123Notes_3p5_annotated.pdf"],
      ["2026-10-07T11:00:00","math123Notes_3p6_annotated.pdf"],
      ["2026-10-21T11:00:00","math123Notes_4p1_annotated.pdf"],
      ["2026-10-27T11:00:00","math123Notes_4p2_annotated.pdf"],
      ["2026-10-29T11:00:00","math123Notes_4p4_annotated.pdf"],
      ["2026-11-02T11:00:00","math123Notes_4p5_annotated.pdf"],
      ["2026-11-05T11:00:00","math123Notes_5p4_annotated.pdf"],
      ["2026-11-10T11:00:00","math123Notes_5p5_annotated.pdf"],
      ["2026-11-11T11:00:00","math123Notes_5p6_annotated.pdf"],
      ["2026-11-20T11:00:00","math123Notes_6p1_annotated.pdf"],
      ["2026-11-30T11:00:00","math123Notes_6p2_annotated.pdf"],
      ["2026-12-02T11:00:00","math123Notes_6p5_annotated.pdf"],
      ]
  show_links_by_date("math123_NoteKeys",releaseDatesList);

  var releaseDatesList=[
      ["2026-01-14T12:00:00","math125Notes_01p1_annotated.pdf"],
      ["2026-01-16T12:00:00","math125Notes_01p2_annotated.pdf"],
      ["2026-01-21T12:00:00","math125Notes_01p3_annotated.pdf"],
      ["2026-01-26T12:00:00","math125Notes_02p1_annotated.pdf"],
      ["2026-01-28T12:00:00","math125Notes_02p2_annotated.pdf"],
      ["2026-02-02T12:00:00","math125Notes_02p5_annotated.pdf"],
      ["2026-02-04T12:00:00","math125Notes_03p1_annotated.pdf"],
      ["2026-02-09T12:00:00","math125Notes_03p2_annotated.pdf"],
      ["2026-02-16T12:00:00","math125Notes_06p1_annotated.pdf"],
      ["2026-02-20T12:00:00","math125Notes_06p4_annotated.pdf"],
      ["2026-02-23T12:00:00","math125Notes_08p1_annotated.pdf"],
      ["2026-02-25T12:00:00","math125Notes_08p2_annotated.pdf"],
      ["2026-03-09T12:00:00","math125Notes_08p3_annotated.pdf"],
      ["2026-03-11T12:00:00","math125Notes_08p4_annotated.pdf"],
      ["2026-03-13T12:00:00","math125Notes_08p5_annotated.pdf"],
      ["2026-03-23T12:00:00","math125Notes_01p4_annotated.pdf"],
      ["2026-03-25T12:00:00","math125Notes_04p9_annotated.pdf"],
      ["2026-03-27T12:00:00","math125Notes_10p2_annotated.pdf"],
      ["2026-03-30T12:00:00","math125Notes_10p4_annotated.pdf"],
      ["2026-04-01T12:00:00","math125Notes_10p5_annotated.pdf"],
      ["2026-04-01T12:00:00","math125Notes_10p6_annotated.pdf"],
      ["2026-04-06T12:00:00","math125Notes_07p1_annotated.pdf"],
      ["2026-04-08T12:00:00","math125Notes_07p2_annotated.pdf"],
      ["2026-04-10T12:00:00","math125Notes_05p1_annotated.pdf"],
      ["2026-04-13T12:00:00","math125Notes_05p6_annotated.pdf"],
      ["2026-04-15T12:00:00","math125Notes_09p1_annotated.pdf"],
      ["2026-04-20T12:00:00","math125Notes_10p1_annotated.pdf"],
      ["2026-04-22T12:00:00","math125Notes_10p3_annotated.pdf"],
      ]
  show_links_by_date("math125_NoteKeys",releaseDatesList);

  var releaseDatesList=[
      ["2026-08-20T14:30:00","math211Notes_1p1_annotated.pdf"],
      ["2026-08-25T14:30:00","math211Notes_1p2_1p4_1p5_annotated.pdf"],
      ["2026-09-01T14:30:00","math211Notes_2p1_2p2_2p3_annotated.pdf"],
      ["2026-09-01T14:30:00","math211Notes_2p4_2p5_annotated.pdf"],
      ["2026-09-08T14:30:00","math211Notes_3p1_annotated.pdf"],
      ["2026-09-10T14:30:00","math211Notes_3p2_3p3_annotated.pdf"],
      ["2026-09-15T14:30:00","math211Notes_3p4_3p5_annotated.pdf"],
      ["2026-09-24T14:30:00","math211Notes_4p1_4p2_annotated.pdf"],
      ["2026-09-29T14:30:00","math211Notes_4p3_4p4_annotated.pdf"],
      ["2026-10-13T14:30:00","math211Notes_6p1_6p2_annotated.pdf"],
      ["2026-10-20T14:30:00","math211Notes_7p1_7p2_7p3_annotated.pdf"],
      ["2026-10-29T14:30:00","math211Notes_7p4_8p1_8p2_annotated.pdf"],
      ["2026-11-05T14:30:00","math211Notes_8p3_9p1_9p2_annotated.pdf"],
      ["2026-11-10T14:30:00","math211Notes_9p3_annotated.pdf"],
      ["2026-11-12T14:30:00","math211Notes_9p4_annotated.pdf"],
      ]
  show_links_by_date("math211_NoteKeys",releaseDatesList);
</script>