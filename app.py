#!/usr/bin/env python3.12
# rmb —— 填个金额，直接出人民币大写；写报销单、合同不用再数笔画
# 纯前端算，这里只发一个空壳页面
import os

from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("page.html")


@app.get("/healthz")
def healthz():
    return "ok"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("RMB_PORT", "8883")), debug=False)
