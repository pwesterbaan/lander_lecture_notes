<h1>Dr. Westerbaan's Lecture Notes</h1>

Below are links to notes used at Lander University:

{% for class in list_of_class_dicts %}
<h1> {{ class.get('name') }} </h1>

<a href=https://github.com/pwesterbaan/lander_lecture_notes/raw/main/{{ class.get('file_name') }}>{{ class.get('file_name') }}</a>

<details>
  <summary>{{ class.get('name') }} Annotated Notes</summary>
    <ul>{% for file in class.get('list_of_pdfs') %}
      <li><a href={{ class.get('base_url') }}/{{ file }}>{{ file }}</a></li>{% endfor %}
    </ul>
</details>
{% endfor %}