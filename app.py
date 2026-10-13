import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cấu hình trang web
st.set_page_config(
    page_title="Quan_ly_diem_sinh_vien",
    page_icon="🎓",
    layout="wide"
)

# Tiêu đề
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Ứng dụng quản lý và thống kê kết quả học tập của sinh viên")

# Dữ liệu sinh viên
data = {
    "Họ và tên": [
        "Nguyễn Văn An",
        "Trần Thị Bình",
        "Lê Hoàng Cường",
        "Phạm Minh Dũng",
        "Võ Ngọc Hà",
        "Đặng Quốc Huy",
        "Bùi Thu Lan",
        "Hồ Minh Nam",
        "Đỗ Thanh Phương",
        "Nguyễn Gia Bảo"
    ],
    "Điểm chuyên cần": [9, 8, 7, 9, 10, 6, 8, 5, 7, 9],
    "Điểm giữa kỳ":    [8, 7, 6, 9, 9, 5, 8, 4, 6, 8],
    "Điểm cuối kỳ":    [9, 8, 5, 9, 10, 4, 7, 3, 5, 9]
}
df = pd.DataFrame(data)

# Tính điểm tổng kết
df["Tổng kết"] = (
    + 0.2 * df["Điểm chuyên cần"]
    + 0.3 * df["Điểm giữa kỳ"]
    + 0.5 * df["Điểm cuối kỳ"]
)

# Xếp loại
def xep_loai(điểm):
    if điểm >= 8.5:
        return "Giỏi"
    elif điểm >= 7.0:
        return "Khá"
    elif điểm >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)


# Bảng điểm
st.subheader("1. Bảng điểm sinh viên")

bang_diem = df.rename(columns={
    "Ho_va_ten": "Họ và tên",
    "Diem_chuyen_can": "Điểm chuyên cần",
    "Diem_giua_ky": "Điểm giữa kỳ",
    "Diem_cuoi_ky": "Điểm cuối kỳ",
    "Diem_tong_ket": "Điểm tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(bang_diem, use_container_width=True, hide_index=True)

# Thống kê
st.subheader("2. Thống kê kết quả học tập")

dtk_trung_binh = df['Tổng kết'].mean()
sv_max = df.loc[df['Tổng kết'].idxmax()]
sv_min = df.loc[df['Tổng kết'].idxmin()]
so_sv_dat = (df['Tổng kết'] >= 5).sum()

cot1, cot2, cot3, cot4 = st.columns(4)

cot1.metric("Điểm trung bình lớp", f"{diem_tb:.2f}")
cot2.metric("Điểm cao nhất", f"{sv_max['Tổng kết']:.2f}")
cot3.metric("Điểm thấp nhất", f"{sv_min['Tổng kết']:.2f}")
cot4.metric("Số sinh viên đạt", f"{so_sv_dat}/{len(df)}")

st.write(
    f"**Sinh viên cao điểm nhất:** {sv_max['Họ và tên']}"
)
st.write(
    f"**Sinh viên thấp điểm nhất:** {sv_min['Họ và tên']}"
)

# Tra cứu sinh viên
st.subheader("3. Tra cứu điểm sinh viên")

ten_sv = st.selectbox(
    "Chọn sinh viên:",
    df["Ho_va_ten"].tolist()
)

sv = df[df["Ho_va_ten"] == ten_sv].iloc[0]

st.write(f"**Họ và tên:** {sv['Ho_va_ten']}")
st.write(f"**Điểm chuyên cần:** {sv['Chuyen_can']}")
st.write(f"**Điểm giữa kỳ:** {sv['Giua_ky']}")
st.write(f"**Điểm cuối kỳ:** {sv['Cuoi_ky']}")
st.write(f"**Điểm tổng kết:** {sv['Tong_ket']:.2f}")
st.write(f"**Xếp loại:** {sv['Xep_loai']}")

# Biểu đồ
st.subheader("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho_va_ten"], df["Tong_ket"])
ax.set_xlabel("Họ và tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.set_title("Điểm tổng kết của sinh viên")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)
plt.close(fig)

# Thông tin người thực hiện
st.markdown("---")
st.caption("Người thực hiện: [Trần Thảo Nguyên] | MSSV: [034308005158]")
