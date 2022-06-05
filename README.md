Open the file in VScode EXPLORER

For Mac(have installed python3 , pip3 and virtualenv):

run (python3 -m venv env) to create a virtual env
run (source ./env/bin/activate)
install streamlit: pip3 install streamlit or pip install streamlit
run (streamlit run alcoholPredict.py)
if error: No module named 'sklearn', run (pip install -U scikit-learn scipy matplotlib) to install
finally, run (streamlit run app.py)

to deactivate: deactivate


For Windows (If python(python3) is installed in your system):

To install streamlit, follow the page: https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-windows

Video tutorial: https://www.youtube.com/watch?v=Vu5Bw745vXg

After installing the Anaconda Navigator, luach the navifator, go to Enviroments, click the Create button bellow to create a new enviroment(for example, called streamlit).
Then press the green start button, choose open with Terminal

On the terminal side:

run (pip install streamlit), wait til it successfully installed.
use (cd) command go the directory where you saved the folder that contains alcoholPredict.py, app.py, README.md, saved_steps.pkl files
run (streamlit run app.py) to luanch the web app
if error: No module named 'sklearn' occurs, run (pip install -U scikit-learn scipy matplotlib) to install
then run (streamlit run app.py) to luanch the web app again

