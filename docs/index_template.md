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

<ul>{% for class_dict in list_of_class_dicts %}
<h1> {{ class_dict.get('name') }} </h1>

<li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/{{ class_dict.get('file_name') }}" target="_blank">{{ class_dict.get('file_name') }}</a></li>
{% if class_dict.get('list_of_pdfs')|length >0 %}
<details name="annotated_notes">
  <summary>{{ class_dict.get('name') }} Annotated Notes (click to expand)</summary>
    <ul id="{{class_dict.get('list_id')}}">
      <script> add_links_by_date("{{class_dict.get('list_id')}}",[
      {% for file in class_dict.get('list_of_pdfs') %}["{{class_dict.get('release_date').get(file,'')}}","{{file}}"],
      {% endfor %}])</script>
    </ul>
</details>
{% endif %}
{% endfor %}
</ul>
