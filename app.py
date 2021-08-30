import streamlit as st
from easyocr_utils import show_uploaded_file, ocr_reader, read_image, language_mapping

st.title("Indic OCR - OCR for Indian Languages")
st.caption("Powered by EasyOCR and Streamlit")
st.caption("Made with opensource ❤️ by @whisperingwasps")


open_cv_image=""
all_languages_selected=""
easyocr_bounding_process_status=""
ocr_result=""
loading_ocr_complete = False


st.sidebar.subheader("Configuration Options")

is_image_uploaded = st.sidebar.file_uploader('Upload the file to perform OCR')

if is_image_uploaded:
    image_name = is_image_uploaded.name
    st.success("Image "+image_name+" has been uploaded")
    open_cv_image = show_uploaded_file(is_image_uploaded)

    st.sidebar.text(" ")

    if st.sidebar.checkbox('Show the uploaded image'):
        st.image(open_cv_image, channels="BGR")

    st.sidebar.markdown("***")

    tooltip_markdown = '''
        Select the language to perform Indic OCR on
    '''.strip()

    languages_selected = st.sidebar.multiselect('Choose the language to perform OCR', ["Hindi", "Tamil", "Telugu", "Kannada", "Bihari", "Bhojpuri", "Bengali", "Goan Konkani", "Marathi", "Urdu" ], help=tooltip_markdown)
    
    if languages_selected:
        all_languages_selected = st.sidebar.button("Perform Indic OCR")

    #st.write(languages_selected)
    #st.write(all_languages_selected)

    st.sidebar.markdown("***")
 
    if all_languages_selected:
        with st.expander("Perform OCR", expanded=True):            
            
            with st.spinner("It takes some time to perform OCR if you are on a CPU, this module is much faster on a GPU"):
                loading_ocr_complete = True
                st.info("Performing OCR on the uploaded image....")
                lang_list = language_mapping(languages_selected)
                #st.write(lang_list)
                #lang_list = ['en']
                ocr_reader_model = ocr_reader(lang_list)
                ocr_result = read_image(ocr_reader_model,open_cv_image)
                easyocr_bounding_process_status = True
                st.success("Indic OCR completed successfully!")
                st.balloons()
            
    if loading_ocr_complete is True:
        with st.expander("View Indic OCR results", expanded=False):
            st.info("Column Details: 0 -> Bounding Box Co-ordinates, 1 -> Detected Text, 2 -> Detection Confidence")
            cropped_text_status = st.table(ocr_result)

        
else:
    st.warning("Please upload an image in the left pane")
    





