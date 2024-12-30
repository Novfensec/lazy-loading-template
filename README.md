# Lazy Loading Template for Kivy and KivyMD apps

## Overview
This repository contains a basic KivyMD app generated with a sequence of [KvDeveloper CLI](https://github.com/Novfensec/KvDeveloper) commands and some extra changes to enable lazy-loading of screens by using one of the KvDeveloper components named `LazyManager`.

## Prerequisites
Make sure you have the following installed:

  + **Kivy** : A Python framework for creating cross-platform applications.
  + **KivyMD** : A library providing Material Design components for Kivy.
  + **KvDeveloper** : Command line interface for managing Kivy and KivyMD applications.

## Installation
1. Install `Kivy>=2.3.0 (specific)`, `KivyMD>=2.0.1.dev0 (specific)`, `KvDeveloper>=2024.1.9.dev0`

   <pre class="language-markup"><code>pip install kivy==2.3.0 https://github.com/kivymd/KivyMD/archive/master.zip https://github.com/Novfensec/KvDeveloper/archive/main.zip</code></pre>

## Usage
1. Run the KivyMD app using terminal:

   - Activate Virtual Environment.

      <pre class="language-markup"><code>venv\scripts\activate</code></pre>

   - Run the App.

      <pre class="language-markup"><code>(venv) python main.py</code></pre>

2. Simply execute the `main.py` file from your editor in a python debug terminal.

You should see the app window open with some basic app design.

Happy Coding!
