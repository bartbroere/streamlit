# Copyright (c) Streamlit Inc. (2018-2023) Snowflake Inc. (2023)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit import runtime


st.header("Main Page with static files")

if not st.get_option("server.enableStaticServing") or \
    not st.get_option("server.maxStaticFileSize"):
    st.error(
        """
        **ERROR**. This test needs to be run with `--server.enableStaticServing` 
        and `--server.maxStaticFileSize`, like this:

        ```
        streamlit run
            e2e/scripts/staticfiles_apps/streamlit_static_with_limit.py
            --server.enableStaticServing=true
            --server.maxStaticFileSize=1
        ```
    """
    )

elif runtime.exists():
    """Static files serving works only when runtime exists"""
    st.markdown(
        "![Streamlit](http://localhost:8501/app/static/streamlit-mark-color.png)"
    )