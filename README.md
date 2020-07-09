<h1>MaxMovie</h1>
A way to get max. money by picking the right movies in a given year.
<h2>Prerequisites</h2>
Python 3+ <br>

<h2>Installing</h2>
A step by step series of examples that tell you how to get a development env running.<br>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>Running the project</h2>
How to run the project
In the project dir
<pre><code>python manage.py runserver</code></pre>

<h2>Input JSON format </h2>
<pre><code>
{"movie_list":
            {
                "Unique Key":{"movie":"*Name of movie*",
                    "start_date":"*date Month(Jan, Feb, etc*)",
                    "end_date":"*date Month(Jan, Feb, etc*)"},
            }
}
</code></pre>
Input Example
<pre><code>
{"movie_list":
            {
                "1":{"movie":"Rock",
                    "start_date":"20 Jan",
                    "end_date":"30 Jan"},
            }
}
</code></pre>

<h2>Output JSON format </h2>
<pre><code>
{"movie_list":
            {
                "Unique Key":{"movie":"*Name of movie*",
                    "start_date":"*date Month(Jan, Feb, etc*)",
                    "end_date":"*date Month(Jan, Feb, etc*)"},
            }
}
</code></pre>
