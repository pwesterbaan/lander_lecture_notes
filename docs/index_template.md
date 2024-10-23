<h1>Dr. Westerbaan's Lecture Notes</h1>

Below are links to notes used at Lander University:

<ul>{% for class in list_of_class_dicts %}
<h1> {{ class.get('name') }} </h1>

<li><a href="https://github.com/pwesterbaan/lander_lecture_notes/raw/main/{{ class.get('file_name') }}" target="_blank">{{ class.get('file_name') }}</a></li>

<details name="annotated_notes">
  <summary>{{ class.get('name') }} Annotated Notes</summary>

<ul>{% for file in class.get('list_of_pdfs') %}
<li><a href="{{ class.get('base_url') }}{{ file }}">{{ file }}</a></li>
{% endfor %}
</ul>
</details>

{% endfor %}
</ul>