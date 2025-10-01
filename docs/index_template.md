<script>
    function add_link_by_date(listId,dispDate,urlString){
        if (new Date() >= new Date(dispDate)){
            // TODO: Clean up this Javascript. This works for now, but creating "myItem" might be excessive?

            const segments = new URL(urlString).pathname.split('/');
            const fileName = segments.pop() || segments.pop(); // Handle potential trailing slash

            const myLink=document.createElement('a');
            myLink.href = urlString;
            myLink.text = fileName;
            myLink.target = "_blank"

            const myItem=document.createElement('li');
            myItem.append(myLink);
            document.getElementById(listId).append(myItem);
        }
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

  <ul id="{{class_dict.get('list_id')}}">{% for file in class_dict.get('list_of_pdfs') %}
    <script> add_link_by_date("{{class_dict.get('list_id')}}","{{class_dict.get('release_date').get(file,'')}}","{{class_dict.get('base_url')}}{{file}}")</script>
{% endfor %}
  </ul>
</details>

{% endif %}
{% endfor %}
</ul>