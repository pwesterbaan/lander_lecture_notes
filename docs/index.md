<script>
    // For anyone looking at this:
    // Obviously this is not a secure way to hide links
    // I'm hiding these links to encourage my students
    // to actually take notes and pay attention during class
    function add_links_by_date(noteKeysDir,dateUrlArray){
      baseURL="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/";
      annNotesDir=noteKeysDir+"/annotated_notes/";
        dateUrlArray.forEach(element => {
          [dispDate, fileName]=element;
          if (new Date() >= new Date(dispDate)){
            // TODO: Clean up this Javascript. This works for now, but creating "myItem" might be excessive?

            const myLink=document.createElement('a');
            myLink.href = new URL(fileName,baseURL+annNotesDir);
            myLink.text = fileName;
            myLink.target = "_blank"

            const myItem=document.createElement('li');
            myItem.append(myLink);
            document.getElementById(noteKeysDir).append(myItem);
          };
        });
    }
</script>

<h1>Dr. Westerbaan's Lecture Notes</h1>

Below are links to notes used at Lander University:

<ul>
<h1> math121 </h1>

<li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math121Notes.pdf" target="_blank">math121Notes.pdf</a></li>

<details name="annotated_notes">
  <summary>math121 Annotated Notes (click to expand)</summary>
    <ul id="math121_NoteKeys">
      <script> add_links_by_date("math121_NoteKeys",[
      ["2025-08-25T13:00:00","mathApp_harshbarger_1p1_annotated.pdf"],
      ["2025-08-27T13:00:00","mathApp_harshbarger_1p3_annotated.pdf"],
      ["2025-08-29T13:00:00","mathApp_harshbarger_1p4_annotated.pdf"],
      ["2025-09-05T13:00:00","mathApp_harshbarger_1p5_annotated.pdf"],
      ["2025-09-12T13:00:00","mathApp_harshbarger_1p6_annotated.pdf"],
      ["2025-11-19T13:00:00","mathApp_harshbarger_2p1_annotated.pdf"],
      ["2025-11-21T13:00:00","mathApp_harshbarger_2p2_annotated.pdf"],
      ["2025-12-03T13:00:00","mathApp_harshbarger_2p3_annotated.pdf"],
      ["2025-09-24T13:00:00","mathApp_harshbarger_4p1_annotated.pdf"],
      ["2025-09-29T13:00:00","mathApp_harshbarger_4p2_annotated.pdf"],
      ["2025-10-06T13:00:00","mathApp_harshbarger_5p1_annotated.pdf"],
      ["2025-10-10T13:00:00","mathApp_harshbarger_5p2_annotated.pdf"],
      ["2025-10-15T13:00:00","mathApp_harshbarger_5p3_annotated.pdf"],
      ["2025-10-24T13:00:00","mathApp_harshbarger_6p1_annotated.pdf"],
      ["2025-10-29T13:00:00","mathApp_harshbarger_6p2_annotated.pdf"],
      ["2025-11-03T13:00:00","mathApp_harshbarger_6p3_annotated.pdf"],
      ["3000-11-12T13:00:00","mathApp_harshbarger_6p4_annotated.pdf"],
      ["2025-11-08T13:00:00","mathApp_harshbarger_6p5_annotated.pdf"],
      ])</script>
    </ul>
</details>


<h1> math123 </h1>

<li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math123Notes.pdf" target="_blank">math123Notes.pdf</a></li>

<details name="annotated_notes">
  <summary>math123 Annotated Notes (click to expand)</summary>
    <ul id="math123_NoteKeys">
      <script> add_links_by_date("math123_NoteKeys",[
      ["2025-08-23T09:00:00","math123Notes_1p4_annotated.pdf"],
      ["2025-08-26T09:00:00","math123Notes_2p1_annotated.pdf"],
      ["2025-08-28T09:00:00","math123Notes_2p2_annotated.pdf"],
      ["2025-09-06T09:00:00","math123Notes_2p4_annotated.pdf"],
      ["2025-08-11T09:00:00","math123Notes_2p5_annotated.pdf"],
      ["2025-08-16T09:00:00","math123Notes_2p6_annotated.pdf"],
      ["2025-09-25T09:00:00","math123Notes_3p1_annotated.pdf"],
      ["2025-09-27T09:00:00","math123Notes_3p2_annotated.pdf"],
      ["2025-09-30T09:00:00","math123Notes_3p3_annotated.pdf"],
      ["2025-10-15T09:00:00","math123Notes_3p5_annotated.pdf"],
      ["2025-10-07T09:00:00","math123Notes_3p6_annotated.pdf"],
      ["2025-10-24T09:00:00","math123Notes_4p1_annotated.pdf"],
      ["2025-10-27T09:00:00","math123Notes_4p2_annotated.pdf"],
      ["2025-10-29T09:00:00","math123Notes_4p4_annotated.pdf"],
      ["2025-11-03T09:00:00","math123Notes_4p5_annotated.pdf"],
      ])</script>
    </ul>
</details>


<h1> math211 </h1>

<li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/math211Notes.pdf" target="_blank">math211Notes.pdf</a></li>

<details name="annotated_notes">
  <summary>math211 Annotated Notes (click to expand)</summary>
    <ul id="math211_NoteKeys">
      <script> add_links_by_date("math211_NoteKeys",[
      ["2025-08-19T11:00:00","math211Notes_1p1_annotated.pdf"],
      ["2025-08-21T11:00:00","math211Notes_1p2_1p4_1p5_annotated.pdf"],
      ["2025-08-26T11:00:00","math211Notes_2p1_2p2_2p3_annotated.pdf"],
      ["2025-08-28T11:00:00","math211Notes_2p4_2p5_annotated.pdf"],
      ["2025-09-04T11:00:00","math211Notes_3p1_annotated.pdf"],
      ["2025-09-09T11:00:00","math211Notes_3p2_3p3_annotated.pdf"],
      ["2025-09-11T11:00:00","math211Notes_3p4_3p5_annotated.pdf"],
      ["2025-09-23T11:00:00","math211Notes_4p1_4p2_annotated.pdf"],
      ["2025-09-25T11:00:00","math211Notes_4p3_4p4_annotated.pdf"],
      ["2025-10-02T11:00:00","math211Notes_6p1_6p2_annotated.pdf"],
      ["2025-10-09T11:00:00","math211Notes_7p1_7p2_7p3_annotated.pdf"],
      ["2025-10-28T11:00:00","math211Notes_7p4_8p1_8p2_annotated.pdf"],
      ["2025-10-30T11:00:00","math211Notes_8p3_9p1_9p2_annotated.pdf"],
      ["2025-11-04T11:00:00","math211Notes_9p3_annotated.pdf"],
      ["2025-11-06T11:00:00","math211Notes_9p4_annotated.pdf"],
      ])</script>
    </ul>
</details>


</ul>