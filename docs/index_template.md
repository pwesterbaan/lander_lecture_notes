<h1>Dr. Westerbaan's Lecture Notes</h1>

Below are links to notes used at Lander University:

<ul>{% for class_dict in list_of_class_dicts %}
<h1> {{ class_dict.get('name') }} </h1>

<li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/{{ class_dict.get('file_name') }}" target="_blank">{{ class_dict.get('file_name') }}</a></li>

{% if class_dict.get('list_of_pdfs')|length >0 %}
<details name="annotated_notes">
  <summary>{{ class_dict.get('name') }} Annotated Notes</summary>

<ul>{% for file in class_dict.get('list_of_pdfs') %}
<li><a href="{{ class_dict.get('base_url') }}{{ file }}" target="_blank">{{ file }}</a></li>
{% endfor %}
</ul>
</details>

{% endif %}
{% endfor %}
</ul>