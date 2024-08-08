import streamlit as st
import modules.functions as functions

todos = functions.read_todos("app1/todos.txt")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos, "app1/todos.txt")


st.title("My To-Do App")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos, "app1/todos.txt")
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")