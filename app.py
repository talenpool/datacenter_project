# Bismillahirrahumanirrahim

import streamlit as st
from PIL import Image
import json
from streamlit_drawable_canvas import st_canvas

# Page layout
st.set_page_config(layout="wide")
st.title("Interactive Layout Mapping App")

# Choose layout type
layout_type = st.selectbox("Choose Layout Mode", ["Office", "Data Center"])

# Load correct layout and assets
if layout_type == "Office":

    # Image.open("assets/office/ren_floorplan.png").show()
    # try:
    #     base_image = Image.open("assets/office/floorplan.png")
    # except Exception:
    #     base_image = Image.new("RGB", (1000, 600), color="gray")
    #     st.warning("Could not load floorplan image - assets/office/floorplan.png. Using placeholder.")

    base_image = Image.open("assets/office/floorplan.png")
    # asset_paths = {
    #     "Desk": "assets/office/desk.png",
    #     "Computer": "assets/office/computer.png",
    #     "Printer": "assets/office/printer.png",
    #     "Telephone": "assets/office/telephone.png"
    # }
    # st.write("In Offfice Layout")
else:
    base_image = Image.open("assets/datacenter/test888.png")
    # asset_paths = {
    #     "Rack": "assets/datacenter/rack.png",
    #     "Server": "assets/datacenter/server.png",
    #     "Patch Panel": "assets/datacenter/patch_panel.png",
    #     "Switch": "assets/datacenter/switch.png"
    # }
    # st.write("In Else Part")

# from PIL import Image
# from streamlit_drawable_canvas import st_canvas

placeholder = Image.new("RGBA", (1000, 600), color="lightgray")

canvas_result = st_canvas(
    background_image=placeholder,
    update_streamlit=True,
    height=600,
    width=1000,
    drawing_mode="transform",
    key="canvas"
)


# st.image(base_image, caption="Floorplan Preview", use_column_width=True)

# test_image = Image.new("RGBA", (1000, 600), color="lightgray")

# # Canvas widget
# canvas_result = st_canvas(
#     background_image=test_image,
#     stroke_width=1,
#     drawing_mode="transform",
#     height=600,
#     width=1000,
#     update_streamlit=True,
#     key=f"{layout_type}_canvas"
# )

# base_image = Image.open("assets/office/floorplan.png").convert("RGBA")
# base_image = base_image.resize((1000, 600))  # Match canvas size

# Canvas widget
# canvas_result = st_canvas(
#     background_image=base_image,
#     stroke_width=1,
#     drawing_mode="transform",
#     height=600,
#     width=1000,
#     update_streamlit=True,
#     key=f"{layout_type}_canvas"
# )

# canvas_result = st_canvas(
#     background_image=base_image,
#     update_streamlit=True,
#     height=600,
#     width=1000,
#     drawing_mode="transform",
#     key="canvas"
# )

# # Asset selection
# selected_asset = st.selectbox("Choose Asset to Place", list(asset_paths.keys()))
# uploaded_asset = Image.open(asset_paths[selected_asset])
# st.image(uploaded_asset, caption=f"{selected_asset} Preview", width=150)

# # Save asset positions
# if st.button("Save Asset Positions"):
#     with open("data/asset_positions.json", "w") as f:
#         json.dump(canvas_result.json_data["objects"], f)
#     st.success("Asset positions saved.")

# # Export layout view
# if st.button("Export as Image"):
#     from matplotlib import pyplot as plt
#     fig, ax = plt.subplots()
#     ax.imshow(base_image)
#     for obj in canvas_result.json_data.get("objects", []):
#         ax.text(obj["left"], obj["top"], obj["type"])
#     ax.axis("off")
#     plt.savefig("exported_layout.png", bbox_inches="tight")
#     st.success("Layout exported as exported_layout.png")
