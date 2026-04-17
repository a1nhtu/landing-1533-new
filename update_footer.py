import re

with open('e:/AntiGravity/May-cham-cong/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_footer_html = """    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <!-- Column 1 -->
                <div class="footer-col">
                    <h3 class="footer-title">DigiPlus</h3>
                    <p class="footer-desc">Đối tác phân phối chính hãng máy chấm công và thiết bị kiểm soát cửa ra vào. Cung cấp giải pháp quản lý nhân sự toàn diện cho doanh nghiệp Việt Nam.</p>
                    <div class="footer-certs">
                        <span>Chứng nhận:</span>
                        <span class="cert-badge">ISO</span>
                        <span class="cert-badge">CE</span>
                        <span class="cert-badge">FCC</span>
                        <span class="cert-badge">RoHS</span>
                    </div>
                </div>
                <!-- Column 2 -->
                <div class="footer-col" style="padding-top: 5px;">
                    <h3 class="footer-title" style="font-size: 1.1rem; margin-bottom: 1.5rem;">Liên Hệ</h3>
                    <ul class="footer-links">
                        <li><i class="fas fa-phone-alt"></i> 0964 523 531 (Hotline)</li>
                        <li><i class="fab fa-zalo"></i> 0372.669.992 (Zalo)</li>
                        <li><i class="fas fa-envelope"></i> tudigiplus.vn@gmail.com</li>
                    </ul>
                </div>
                <!-- Column 3 -->
                <div class="footer-col" style="padding-top: 5px;">
                    <h3 class="footer-title" style="font-size: 1.1rem; margin-bottom: 1.5rem;">Hotline Tư Vấn</h3>
                    <div class="footer-hotline-box">
                        <div class="fh-number">0964.523.531</div>
                        <div class="fh-text">Hỗ trợ 24/7</div>
                    </div>
                    <p class="footer-address">
                        <i class="fas fa-map-marker-alt"></i> Trụ sở chính: 93 ngõ 72, Tôn Thất Tùng, Hà Nội
                    </p>
                    <div class="footer-social">
                        <a href="https://www.facebook.com/Digiplus.vn/" class="social-icon fb"><i class="fab fa-facebook-f"></i></a>
                        <a href="https://zalo.me/0372669992" class="social-icon zl"><span class="zalo-text-icon" style="font-size: 0.6rem; color: #fff;">Zalo</span></a>
                        <a href="tel:0964523531" class="social-icon ph"><i class="fas fa-phone-alt"></i></a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 DIGIPLUS - Hệ thống máy chấm công chuyên nghiệp</p>
            </div>
        </div>
    </footer>"""

html = re.sub(r'    <footer class="footer">.*?</script>\n</body>', new_footer_html + '\n\n' + r'    <!-- Floating Contact Buttons -->' + '\n' + r'    <div class="floating-contact">' + '\n' + html.split('<div class="floating-contact">')[1], html, flags=re.DOTALL)

with open('e:/AntiGravity/May-cham-cong/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('e:/AntiGravity/May-cham-cong/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_css = """/* Footer Redesign */
.footer {
    background: #111827 !important;
    color: #9ca3af !important;
    padding: 4rem 0 0 0 !important;
    font-size: 0.95rem;
    text-align: left !important;
}

.footer-grid {
    display: grid;
    grid-template-columns: 1.5fr 1fr 1.2fr;
    gap: 3rem;
    margin-bottom: 3rem;
}

.footer-title {
    color: var(--white);
    font-size: 1.5rem;
    font-weight: 700;
}

.footer-desc {
    line-height: 1.8;
    margin-bottom: 1.5rem;
}

.footer-certs {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    flex-wrap: wrap;
}

.cert-badge {
    background: #374151;
    color: #d1d5db;
    padding: 0.3rem 0.6rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
}

.footer-links {
    list-style: none;
    padding: 0;
    margin: 0;
}

.footer-links li {
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    gap: 0.8rem;
}

.footer-hotline-box {
    background: #ef4444;
    color: var(--white);
    padding: 1rem 1.5rem;
    border-radius: 8px;
    margin-bottom: 1.5rem;
    display: inline-block;
    width: 100%;
}

.fh-number {
    font-size: 1.6rem;
    font-weight: 700;
    margin-bottom: 0.2rem;
}

.fh-text {
    font-size: 0.85rem;
    opacity: 0.9;
}

.footer-address {
    line-height: 1.6;
    margin-bottom: 1.5rem;
    display: flex;
    gap: 0.6rem;
    align-items: flex-start;
}

.footer-address i {
    margin-top: 0.3rem;
}

.footer-social {
    display: flex;
    gap: 0.8rem;
}

.social-icon {
    width: 35px;
    height: 35px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--white);
    text-decoration: none;
    font-size: 1rem;
    transition: var(--transition);
}

.social-icon:hover {
    transform: translateY(-3px);
    color: white;
}

.social-icon.fb { background: #1877f2; }
.social-icon.zl { background: #0084ff; }
.social-icon.ph { background: #ef4444; }

.footer-bottom {
    border-top: 1px solid #1f2937 !important;
    padding: 1.5rem 0 !important;
    text-align: center;
    font-size: 0.85rem;
}
@media (max-width: 900px) {
    .footer-grid {
        grid-template-columns: 1fr;
        gap: 2rem;
    }
}
"""

css = css.replace("/* Floating Contact Buttons */", new_css + "\n/* Floating Contact Buttons */")

with open('e:/AntiGravity/May-cham-cong/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
