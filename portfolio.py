import streamlit as st
import plotly.graph_objects as go
import pandas as pd


# ==========================================
# 1. CLASS DỮ LIỆU ỨNG VIÊN (MODEL - OOP)
# ==========================================
class CandidateProfile:
    def __init__(self):
        self.full_name = "PHẠM DUY LÂN"
        self.title = "KỸ THUẬT VIÊN BẢO DƯỠNG NỘI THẤT TÀU BAY (CABIN MECHANIC TRAINEE)"
        self.dob = "06/06/1995"
        self.phone = "0913 661 995"
        self.email = "duylan66@gmail.com"
        self.address = "Ho Chi Minh City, Vietnam"
        self.english = "IELTS 6.0 (Hạn: 07/2028)"
        self.education = "Higher Diploma in Network Security & System Management (HDNSSM)"
        self.school = "FPT Jetking Việt Nam (2021 - 2026)"

    def get_skills(self):
        return [
            {"name": "Tư duy Kỹ thuật & Cơ khí (Mechanical Aptitude)",
             "desc": "Chẩn đoán sự cố, tư duy hệ thống, đọc CMM, IPC, SRM, dùng dụng cụ cầm tay."},
            {"name": "Tuân thủ Quy trình & An toàn (Safety & Compliance)",
             "desc": "Tuân thủ tuyệt đối SOP, quy định an toàn lao động & tiêu chuẩn quốc tế."},
            {"name": "Năng lực Tiếng Anh Kỹ thuật",
             "desc": "IELTS 6.0 – Đọc tài liệu bảo dưỡng linh kiện, viết báo cáo kỹ thuật."},
            {"name": "Xử lý Sự cố & Khai thác Nhanh (Fast Turnaround)",
             "desc": "Giải quyết sự cố áp lực cao, đảm bảo tiến độ chuyến bay."},
            {"name": "Quản lý Hệ thống & Báo cáo",
             "desc": "Ghi nhật ký bảo trì, theo dõi trạng thái linh kiện trên phần mềm."}
        ]

    def get_experiences(self):
        return [
            {
                "role": "Subject Matter Expert (SME)",
                "company": "CONCENTRIX VIỆT NAM",
                "time": "11/2023 - 12/2024",
                "details": [
                    "Kiểm tra chất lượng vận hành và tính tuân thủ của đội ngũ theo chuẩn SLA.",
                    "Duy trì chỉ số FCR và thời gian xử lý AHT đạt trên mục tiêu 82.5%.",
                    "Quản lý công cụ vận hành, an toàn bảo mật, đảm bảo 100% hướng dẫn chuẩn được thực thi."
                ]
            },
            {
                "role": "Technical Support Specialist / Consultant",
                "company": "CONCENTRIX MALAYSIA",
                "time": "06/2021 - 11/2023",
                "details": [
                    "Chẩn đoán & Troubleshooting phần cứng/phần mềm thiết bị đo lường chính xác (FreeStyle Libre CGM/FGM).",
                    "Kiểm tra tính tuân thủ thông số kỹ thuật quốc tế (ISO 15197:2013, IP27).",
                    "Phân tích dữ liệu hiệu suất thiết bị, xu hướng lỗi và gửi báo cáo cải tiến đến phòng Kỹ thuật (Engineering)."
                ]
            }
        ]

    def get_fpt_jetking_grades(self):
        return pd.DataFrame({
            "Học kỳ / Môn học": [
                "HK1: Networking Essentials", "HK1: Windows Server", "HK1: Routing & Switching",
                "HK2: Red Hat Enterprise Linux", "HK2: Network Security", "HK2: Ethical Hacking",
                "HK3: Cloud Computing (AWS/Azure)", "HK3: Firewalls & Defenses",
                "HK4: IoT & System Security", "HK4: Đồ án Tốt nghiệp (Project)"
            ],
            "Điểm Lý Thuyết": [82, 85, 78, 88, 90, 85, 89, 87, 84, 92],
            "Điểm Thực Hành": [88, 90, 85, 92, 94, 88, 92, 90, 89, 95]
        })


# ==========================================
# 2. CLASS GIAO DIỆN VIETJET AIR (VIEW - OOP)
# ==========================================
class VietjetUITheme:
    @staticmethod
    def apply_custom_css():
        css = """
        <style>
        :root {
            --vj-red: #E30613;
            --vj-yellow: #FFF200;
            --vj-dark-red: #B8000A;
        }

        .stApp {
            background-color: #F8F9FA;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .vj-header {
            background: linear-gradient(90deg, var(--vj-red) 0%, var(--vj-dark-red) 100%);
            color: white;
            padding: 20px 30px;
            border-bottom: 5px solid var(--vj-yellow);
            border-radius: 0 0 15px 15px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            position: relative;
            overflow: hidden;
        }

        .vj-header h1 {
            color: white !important;
            font-weight: 800;
            margin: 0;
            font-size: 28px;
            text-transform: uppercase;
        }

        .vj-header p {
            color: #FFF200;
            font-size: 16px;
            margin-top: 5px;
            font-weight: 600;
        }

        .airplane-track {
            width: 100%;
            height: 50px;
            position: relative;
            overflow: hidden;
            background: #eef2f5;
            border-radius: 8px;
            margin: 15px 0;
            border: 1px dashed #E30613;
        }

        .red-airplane {
            position: absolute;
            top: 5px;
            left: -60px;
            font-size: 32px;
            color: var(--vj-red);
            animation: flyRight 8s linear infinite;
        }

        @keyframes flyRight {
            0% { left: -60px; }
            100% { left: 105%; }
        }

        .vj-card {
            background: white;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid var(--vj-red);
            box-shadow: 0 2px 8px rgba(0,0,0,0.06);
            margin-bottom: 20px;
        }

        .vj-card h3 {
            color: var(--vj-red);
            margin-top: 0;
            font-size: 20px;
        }

        .badge-vj {
            background-color: var(--vj-yellow);
            color: #333;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 10px;
        }
        </style>
        """
        st.markdown(css, unsafe_allow_html=True)

    @staticmethod
    def render_header(profile: CandidateProfile):
        header_html = f"""
        <div class="vj-header">
            <div style="float: right; text-align: right;">
                <span class="badge-vj">VIETJET CAREERS PORTFOLIO</span>
            </div>
            <h1>✈️ {profile.full_name}</h1>
            <p>ỨNG TUYỂN: {profile.title}</p>
        </div>

        <div class="airplane-track">
            <div class="red-airplane">✈</div>
        </div>
        """
        st.markdown(header_html, unsafe_allow_html=True)


# ==========================================
# 3. CLASS ỨNG DỤNG CHÍNH (CONTROLLER - OOP)
# ==========================================
class PortfolioApp:
    def __init__(self):
        self.profile = CandidateProfile()

    def render_sidebar(self):
        st.sidebar.image("https://jobs.vietjetair.com/assets/images/logo.png", width=200)
        st.sidebar.title("📌 THÔNG TIN LIÊN HỆ")
        st.sidebar.write(f"📧 **Email:** {self.profile.email}")
        st.sidebar.write(f"📞 **SĐT:** {self.profile.phone}")
        st.sidebar.write(f"📍 **Địa chỉ:** {self.profile.address}")
        st.sidebar.write(f"🎂 **Ngày sinh:** {self.profile.dob}")
        st.sidebar.write(f"🌐 **Tiếng Anh:** {self.profile.english}")

        st.sidebar.markdown("---")
        st.sidebar.subheader("🏆 Thành Tích Nổi Bật")
        st.sidebar.info(
            "**Employee of the Year 2021**\nVinh danh bởi Giám đốc Dịch vụ Khách hàng (Abbott Malaysia) & Tập đoàn Concentrix.")

    def render_charts(self):
        st.subheader("📊 BẢNG ĐIỂM HỌC TẬP & NĂNG LỰC (FPT JETKING)")
        st.caption("Chương trình Higher Diploma Network Security and System Management (HDNSSM)")

        df = self.profile.get_fpt_jetking_grades()

        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df["Học kỳ / Môn học"],
            y=df["Điểm Lý Thuyết"],
            name="Điểm Lý Thuyết",
            marker_color="#FFF200"
        ))
        fig.add_trace(go.Bar(
            x=df["Học kỳ / Môn học"],
            y=df["Điểm Thực Hành"],
            name="Điểm Thực Hành",
            marker_color="#E30613"
        ))

        fig.update_layout(
            barmode='group',
            title="Kết Quả Học Tập Theo Môn Học (Thực hành & Lý thuyết)",
            xaxis_title="Môn Học / Học Kỳ",
            yaxis_title="Điểm Số (Thang điểm 100)",
            yaxis=dict(range=[0, 100]),
            legend=dict(x=0, y=1.1, orientation="h"),
            margin=dict(l=20, r=20, t=50, b=100),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )

        # Cập nhật tham số use_container_width mới của Streamlit
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("#### 🎯 Biểu đồ Năng lực Kỹ thuật Tổng quan (GARP Radar)")
        categories = ['An ninh mạng', 'Quản trị Hệ thống', 'Troubleshooting', 'Tuân thủ Quy trình',
                      'Tiếng Anh Kỹ thuật']
        fig_radar = go.Figure()
        fig_radar.add_trace(go.Scatterpolar(
            r=[88, 92, 95, 98, 85],
            theta=categories,
            fill='toself',
            fillcolor='rgba(227, 6, 19, 0.3)',
            line=dict(color='#E30613', width=2),
            name='Đánh giá Năng lực'
        ))
        fig_radar.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            showlegend=False
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    def run(self):
        st.set_page_config(
            page_title="Portfolio - Phạm Duy Lân | Vietjet Air Candidate",
            page_icon="✈️",
            layout="wide"
        )

        VietjetUITheme.apply_custom_css()
        VietjetUITheme.render_header(self.profile)

        self.render_sidebar()

        col1, col2 = st.tabs(["📋 HỒ SƠ ỨNG TUYỂN", "📈 BẢNG ĐIỂM & NĂNG LỰC (FPT JETKING)"])

        with col1:
            st.markdown("""
            <div class="vj-card">
                <h3>💡 TƯ DUY & ĐỊNH HƯỚNG CÔNG VIỆC</h3>
                <p>Ứng viên chủ động (Proactive), linh hoạt (Dynamic), sở hữu tư duy phân tích kỹ thuật hệ thống sắc bén cùng nền tảng vững chắc về an toàn quy trình. Sẵn sàng đáp ứng tốt nhất yêu cầu nghiêm ngặt trong công tác bảo dưỡng nội thất tàu bay (Cabin Maintenance) tại Vietjet Air.</p>
            </div>
            """, unsafe_allow_html=True)

            st.subheader("🛠️ KỸ NĂNG CHUYÊN MÔN & THẾ MẠNH")
            skills = self.profile.get_skills()
            for sk in skills:
                st.markdown(f"**• {sk['name']}**: {sk['desc']}")

            st.markdown("---")
            st.subheader("💼 KINH NGHIỆM LÀM VIỆC")
            for exp in self.profile.get_experiences():
                with st.expander(f"🔹 **{exp['role']}** - {exp['company']} ({exp['time']})", expanded=True):
                    for detail in exp['details']:
                        st.write(f"- {detail}")

            st.markdown("---")
            st.subheader("🎓 HỌC VẤN & CHỨNG CHỈ")
            st.write(f"• **Hệ sau Cao Đẳng**: {self.profile.education}")
            st.write(f"• **Trường đào tạo**: {self.profile.school}")
            st.write(f"• **Chứng chỉ Tiếng Anh**: {self.profile.english}")

        with col2:
            self.render_charts()


if __name__ == "__main__":
    app = PortfolioApp()
    app.run()