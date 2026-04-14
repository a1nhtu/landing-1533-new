import re

with open('e:/AntiGravity/May-cham-cong/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

faq_match = re.search(r'    <section class="faq-section">.*?</section>\n', text, re.DOTALL)
contact_match = re.search(r'    <section id="contact" class="contact">.*?</section>\n', text, re.DOTALL)

if faq_match and contact_match:
    faq_str = faq_match.group(0)
    contact_str = contact_match.group(0)
    
    trusted_by_str = """    <section class="trusted-by">
        <div class="container">
            <div class="text-center" style="margin-bottom: 3rem;">
                <h2 class="section-title" style="margin-bottom: 0.5rem;">Được Tin Dùng Bởi Hàng Nghìn Doanh Nghiệp</h2>
                <p class="section-subtitle" style="margin-top: 0;">DigiPlus - Đối tác phân phối chính hãng tại Việt Nam</p>
            </div>
            
            <div class="trusted-grid">
                <!-- Card 1 -->
                <div class="trusted-card">
                    <img src="https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Công ty TNHH ABC">
                    <div class="trusted-card-info">
                        <h4>Công ty TNHH ABC</h4>
                        <p>Quận 7, TP.HCM &bull; 150+ nhân viên</p>
                    </div>
                </div>
                <!-- Card 2 -->
                <div class="trusted-card">
                    <img src="https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Xưởng Sản Xuất XYZ">
                    <div class="trusted-card-info">
                        <h4>Xưởng Sản Xuất XYZ</h4>
                        <p>Bình Dương &bull; 300+ công nhân</p>
                    </div>
                </div>
                <!-- Card 3 -->
                <div class="trusted-card">
                    <img src="https://images.unsplash.com/photo-1497215728101-856f4ea42174?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" alt="Văn phòng DEF">
                    <div class="trusted-card-info">
                        <h4>Văn phòng DEF</h4>
                        <p>Quận 1, TP.HCM &bull; 80+ nhân viên</p>
                    </div>
                </div>
            </div>

            <div class="trusted-badges">
                <div class="t-badge-card">
                    <div class="t-badge-icon"><i class="fas fa-shield-alt" style="color: #ff4d4f;"></i></div>
                    <div class="t-badge-text">
                        <h4>Bảo Hành 12 Tháng</h4>
                        <p>Đổi mới nếu lỗi nhà sản xuất</p>
                    </div>
                </div>
                <div class="t-badge-card">
                    <div class="t-badge-icon"><i class="fas fa-headset" style="color: #ff4d4f;"></i></div>
                    <div class="t-badge-text">
                        <h4>Hỗ Trợ 24/7</h4>
                        <p>Tư vấn kỹ thuật mọi lúc</p>
                    </div>
                </div>
                <div class="t-badge-card">
                    <div class="t-badge-icon"><i class="fas fa-clock" style="color: #ff4d4f;"></i></div>
                    <div class="t-badge-text">
                        <h4>Giao Hàng Nhanh</h4>
                        <p>Lắp đặt trong 24h</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
"""

    original_block = faq_str + "\n" + contact_str
    # Reorder: contact -> trusted-by -> faq
    new_block = contact_str + "\n" + trusted_by_str + "\n" + faq_str
    
    text = text.replace(original_block, new_block)
    
    with open('e:/AntiGravity/May-cham-cong/index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('HTML update successful')
else:
    print('Matches not found')
