// Agente 5 Backend Specialist + Agente 2 Validação Specialist
// Formulário Profissional com Validação Inteligente e Múltiplos Canais

class ProfessionalContactForm {
    constructor() {
        this.form = null;
        this.submitBtn = null;
        this.toastContainer = null;
        this.isSubmitting = false;
        
        // Agente 2 Validação: Configurações de validação
        this.validators = {
            name: {
                required: true,
                minLength: 3,
                maxLength: 100,
                pattern: /^[a-zA-ZÀ-ÿ\s]+$/,
                message: 'Nome deve ter entre 3 e 100 caracteres (apenas letras)'
            },
            email: {
                required: true,
                pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
                message: 'Digite um email válido'
            },
            phone: {
                required: false,
                pattern: /^\(\d{2}\)\s\d{4,5}-\d{4}$/,
                message: 'Formato: (11) 98765-4321'
            },
            company: {
                required: false,
                minLength: 2,
                maxLength: 100,
                message: 'Empresa deve ter entre 2 e 100 caracteres'
            },
            subject: {
                required: true,
                minLength: 5,
                maxLength: 200,
                message: 'Assunto deve ter entre 5 e 200 caracteres'
            },
            message: {
                required: true,
                minLength: 20,
                maxLength: 2000,
                message: 'Mensagem deve ter entre 20 e 2000 caracteres'
            }
        };
        
        this.init();
    }
    
    init() {
        this.createForm();
        this.setupEventListeners();
        this.createToastContainer();
    }
    
    // Agente 1 UX/UI: Criação do formulário profissional
    createForm() {
        const formHTML = `
            <div class="contact-form">
                <div class="form-header">
                    <h2>Entre em Contato</h2>
                    <p>Respondo rapidamente a propostas profissionais e oportunidades de colaboração.</p>
                </div>
                
                <form id="professionalContactForm" novalidate>
                    <div class="form-grid">
                        <!-- Informações Pessoais -->
                        <div class="form-group">
                            <label class="form-label">
                                Nome Completo <span class="required">*</span>
                            </label>
                            <input 
                                type="text" 
                                name="name" 
                                class="form-input" 
                                required
                                placeholder="Seu nome completo"
                                autocomplete="name"
                            >
                            <div class="form-help">
                                <span>👤</span>
                                <span>Nome como aparece em documentos profissionais</span>
                            </div>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">
                                Email Profissional <span class="required">*</span>
                            </label>
                            <input 
                                type="email" 
                                name="email" 
                                class="form-input" 
                                required
                                placeholder="seu.email@empresa.com"
                                autocomplete="email"
                            >
                            <div class="form-help">
                                <span>📧</span>
                                <span>Email corporativo para contato profissional</span>
                            </div>
                        </div>
                        
                        <!-- Contato Adicional -->
                        <div class="form-group">
                            <label class="form-label">
                                Telefone/WhatsApp
                            </label>
                            <input 
                                type="tel" 
                                name="phone" 
                                class="form-input" 
                                placeholder="(11) 98765-4321"
                                autocomplete="tel"
                            >
                            <div class="form-help">
                                <span>📱</span>
                                <span>Opcional: para contato rápido via WhatsApp</span>
                            </div>
                        </div>
                        
                        <div class="form-group">
                            <label class="form-label">
                                Empresa
                            </label>
                            <input 
                                type="text" 
                                name="company" 
                                class="form-input" 
                                placeholder="Nome da sua empresa"
                                autocomplete="organization"
                            >
                            <div class="form-help">
                                <span>🏢</span>
                                <span>Empresa que representa (opcional)</span>
                            </div>
                        </div>
                        
                        <!-- Motivo do Contato -->
                        <div class="form-group full-width">
                            <label class="form-label">
                                Assunto <span class="required">*</span>
                            </label>
                            <select name="subject" class="form-select" required>
                                <option value="">Selecione o motivo do contato</option>
                                <option value="oportunidade">Oportunidade de Carreira</option>
                                <option value="projeto">Proposta de Projeto</option>
                                <option value="consultoria">Consultoria em IA/Cybersecurity</option>
                                <option value="parceria">Parceria Estratégica</option>
                                <option value="palestra">Palestra/Mentoria</option>
                                <option value="outro">Outro</option>
                            </select>
                            <div class="form-help">
                                <span>🎯</span>
                                <span>Selecione o motivo principal do contato</span>
                            </div>
                        </div>
                        
                        <!-- Mensagem -->
                        <div class="form-group full-width">
                            <label class="form-label">
                                Mensagem <span class="required">*</span>
                            </label>
                            <textarea 
                                name="message" 
                                class="form-textarea" 
                                rows="6" 
                                required
                                placeholder="Descreva sua proposta, projeto ou oportunidade..."
                            ></textarea>
                            <div class="form-help">
                                <span>💬</span>
                                <span>Seja específico sobre sua proposta ou necessidade</span>
                            </div>
                            <div class="form-help">
                                <span id="charCount">0 / 2000 caracteres</span>
                            </div>
                        </div>
                        
                        <!-- Anexo -->
                        <div class="form-group full-width">
                            <label class="form-label">
                                Anexo (PDF, DOC, DOCX - máx 5MB)
                            </label>
                            <div class="form-file" id="fileUpload">
                                <input 
                                    type="file" 
                                    name="attachment" 
                                    accept=".pdf,.doc,.docx"
                                    id="fileInput"
                                >
                                <div class="form-file-label">
                                    <span>📎</span>
                                    <span id="fileText">Clique para anexar arquivo ou arraste aqui</span>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Preferência de Contato -->
                        <div class="form-group full-width">
                            <label class="form-label">
                                Preferência de Contato
                            </label>
                            <div class="form-checkbox-group">
                                <label class="form-checkbox-item">
                                    <input type="checkbox" name="contact-preference" value="email" checked>
                                    <span class="form-checkbox-label">Email</span>
                                </label>
                                <label class="form-checkbox-item">
                                    <input type="checkbox" name="contact-preference" value="whatsapp">
                                    <span class="form-checkbox-label">WhatsApp</span>
                                </label>
                                <label class="form-checkbox-item">
                                    <input type="checkbox" name="contact-preference" value="linkedin">
                                    <span class="form-checkbox-label">LinkedIn</span>
                                </label>
                            </div>
                        </div>
                        
                        <!-- Termos -->
                        <div class="form-group full-width">
                            <label class="form-checkbox-item">
                                <input type="checkbox" name="terms" required>
                                <span class="form-checkbox-label">
                                    Concordo com os <a href="#" onclick="event.preventDefault(); this.showTerms(); return false;">termos de privacidade</a> e autorizo o contato profissional <span class="required">*</span>
                                </span>
                            </label>
                        </div>
                    </div>
                    
                    <!-- Botões de Ação -->
                    <div class="form-actions">
                        <button type="submit" class="btn btn-primary" id="submitBtn">
                            <span>📤</span>
                            <span>Enviar Mensagem</span>
                        </button>
                        <button type="button" class="btn btn-secondary" id="clearBtn">
                            <span>🔄</span>
                            <span>Limpar Formulário</span>
                        </button>
                    </div>
                </form>
            </div>
        `;
        
        // Substituir o formulário antigo
        const oldFormSection = document.querySelector('section.section:last-child');
        if (oldFormSection) {
            oldFormSection.innerHTML = formHTML;
        }
        
        this.form = document.getElementById('professionalContactForm');
        this.submitBtn = document.getElementById('submitBtn');
        this.clearBtn = document.getElementById('clearBtn');
    }
    
    // Agente 2 Validação: Setup de event listeners
    setupEventListeners() {
        if (!this.form) return;
        
        // Validação em tempo real
        this.form.querySelectorAll('.form-input, .form-textarea, .form-select').forEach(field => {
            field.addEventListener('blur', () => this.validateField(field));
            field.addEventListener('input', () => this.clearFieldError(field));
        });
        
        // Contador de caracteres
        const messageField = this.form.querySelector('textarea[name="message"]');
        const charCount = document.getElementById('charCount');
        if (messageField && charCount) {
            messageField.addEventListener('input', () => {
                const length = messageField.value.length;
                charCount.textContent = `${length} / 2000 caracteres`;
                charCount.style.color = length > 1800 ? 'var(--accent-warning)' : 'var(--text-muted)';
            });
        }
        
        // Upload de arquivo
        const fileInput = document.getElementById('fileInput');
        if (fileInput) {
            fileInput.addEventListener('change', (e) => this.handleFileUpload(e));
        }
        
        // Drag and drop
        const fileUpload = document.getElementById('fileUpload');
        if (fileUpload) {
            fileUpload.addEventListener('dragover', (e) => {
                e.preventDefault();
                fileUpload.classList.add('drag-over');
            });
            
            fileUpload.addEventListener('dragleave', () => {
                fileUpload.classList.remove('drag-over');
            });
            
            fileUpload.addEventListener('drop', (e) => {
                e.preventDefault();
                fileUpload.classList.remove('drag-over');
                if (e.dataTransfer.files.length > 0) {
                    fileInput.files = e.dataTransfer.files;
                    this.handleFileUpload({ target: fileInput });
                }
            });
        }
        
        // Submit do formulário
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        
        // Limpar formulário
        if (this.clearBtn) {
            this.clearBtn.addEventListener('click', () => this.clearForm());
        }
        
        // Formatação de telefone
        const phoneField = this.form.querySelector('input[name="phone"]');
        if (phoneField) {
            phoneField.addEventListener('input', (e) => this.formatPhone(e));
        }
    }
    
    // Agente 2 Validação: Validação de campo
    validateField(field) {
        const fieldName = field.name;
        const value = field.value.trim();
        const validator = this.validators[fieldName];
        
        if (!validator) return true;
        
        // Limpar mensagens anteriores
        this.clearFieldError(field);
        
        // Validação required
        if (validator.required && !value) {
            this.showFieldError(field, 'Este campo é obrigatório');
            return false;
        }
        
        // Se não é required e está vazio, passa
        if (!validator.required && !value) {
            field.classList.add('success');
            return true;
        }
        
        // Validação de tamanho
        if (validator.minLength && value.length < validator.minLength) {
            this.showFieldError(field, validator.message);
            return false;
        }
        
        if (validator.maxLength && value.length > validator.maxLength) {
            this.showFieldError(field, validator.message);
            return false;
        }
        
        // Validação de padrão
        if (validator.pattern && !validator.pattern.test(value)) {
            this.showFieldError(field, validator.message);
            return false;
        }
        
        // Campo válido
        field.classList.add('success');
        return true;
    }
    
    // Agente 2 Validação: Mostrar erro de campo
    showFieldError(field, message) {
        field.classList.remove('success');
        field.classList.add('error');
        
        // Remover erro anterior
        const existingError = field.parentNode.querySelector('.form-error');
        if (existingError) {
            existingError.remove();
        }
        
        // Adicionar nova mensagem de erro
        const errorDiv = document.createElement('div');
        errorDiv.className = 'form-error';
        errorDiv.innerHTML = `<span>⚠️</span><span>${message}</span>`;
        field.parentNode.appendChild(errorDiv);
    }
    
    // Agente 2 Validação: Limpar erro de campo
    clearFieldError(field) {
        field.classList.remove('error');
        const errorDiv = field.parentNode.querySelector('.form-error');
        if (errorDiv) {
            errorDiv.remove();
        }
    }
    
    // Agente 2 Validação: Formatação de telefone
    formatPhone(e) {
        let value = e.target.value.replace(/\D/g, '');
        
        if (value.length > 0) {
            // Formato: (11) 98765-4321
            if (value.length <= 2) {
                value = `(${value}`;
            } else if (value.length <= 7) {
                value = `(${value.slice(0, 2)}) ${value.slice(2)}`;
            } else {
                value = `(${value.slice(0, 2)}) ${value.slice(2, 7)}-${value.slice(7, 11)}`;
            }
        }
        
        e.target.value = value;
    }
    
    // Agente 5 Backend: Upload de arquivo
    handleFileUpload(e) {
        const file = e.target.files[0];
        const fileText = document.getElementById('fileText');
        const fileUpload = document.getElementById('fileUpload');
        
        if (!file) {
            fileText.textContent = 'Clique para anexar arquivo ou arraste aqui';
            fileUpload.classList.remove('has-file');
            return;
        }
        
        // Validação de tamanho (5MB)
        const maxSize = 5 * 1024 * 1024;
        if (file.size > maxSize) {
            this.showToast('Arquivo muito grande. Máximo permitido: 5MB', 'error');
            e.target.value = '';
            return;
        }
        
        // Validação de tipo
        const allowedTypes = ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'];
        if (!allowedTypes.includes(file.type)) {
            this.showToast('Tipo de arquivo não permitido. Use PDF, DOC ou DOCX', 'error');
            e.target.value = '';
            return;
        }
        
        fileText.textContent = `📎 ${file.name} (${(file.size / 1024).toFixed(1)} KB)`;
        fileUpload.classList.add('has-file');
    }
    
    // Agente 5 Backend: Submit do formulário
    async handleSubmit(e) {
        e.preventDefault();
        
        if (this.isSubmitting) return;
        
        // Validar todos os campos
        const fields = this.form.querySelectorAll('.form-input, .form-textarea, .form-select');
        let isValid = true;
        
        fields.forEach(field => {
            if (!this.validateField(field)) {
                isValid = false;
            }
        });
        
        // Validar termos
        const termsCheckbox = this.form.querySelector('input[name="terms"]');
        if (!termsCheckbox.checked) {
            this.showToast('É necessário aceitar os termos de privacidade', 'error');
            isValid = false;
        }
        
        if (!isValid) {
            this.showToast('Por favor, corrija os erros no formulário', 'error');
            return;
        }
        
        // Coletar dados
        const formData = new FormData(this.form);
        const data = Object.fromEntries(formData);
        
        // Adicionar preferências de contato
        const contactPreferences = Array.from(this.form.querySelectorAll('input[name="contact-preference"]:checked'))
            .map(cb => cb.value);
        data.contactPreferences = contactPreferences;
        
        // Adicionar timestamp
        data.timestamp = new Date().toISOString();
        
        // Mostrar loading
        this.setSubmitting(true);
        
        try {
            // Agente 5 Backend: Múltiplos canais de envio
            await this.sendContact(data);
            this.showToast('Mensagem enviada com sucesso! Entrarei em contato em breve.', 'success');
            this.clearForm();
        } catch (error) {
            console.error('Erro ao enviar:', error);
            this.showToast('Erro ao enviar mensagem. Tente novamente ou contate diretamente.', 'error');
        } finally {
            this.setSubmitting(false);
        }
    }
    
    // Agente 5 Backend: Envio para múltiplos canais
    async sendContact(data) {
        // Preparar mensagem para WhatsApp
        const whatsappMessage = this.formatWhatsAppMessage(data);
        
        // Preparar mensagem para Email
        const emailData = this.formatEmailMessage(data);
        
        // Opção 1: WhatsApp (primário)
        const whatsappUrl = `https://wa.me/5511986395283?text=${encodeURIComponent(whatsappMessage)}`;
        
        // Abrir WhatsApp em nova janela
        window.open(whatsappUrl, '_blank', 'width=600,height=800');
        
        // Opção 2: Email (backup)
        const mailtoUrl = `mailto:carlos.costato@gmail.com?subject=${encodeURIComponent(emailData.subject)}&body=${encodeURIComponent(emailData.body)}`;
        
        // Aguardar um pouco e abrir email como backup
        setTimeout(() => {
            window.open(mailtoUrl, '_blank');
        }, 2000);
        
        // Simular envio para backend (futuro)
        return new Promise((resolve) => {
            setTimeout(resolve, 1000);
        });
    }
    
    // Agente 5 Backend: Formatar mensagem WhatsApp
    formatWhatsAppMessage(data) {
        return `🚀 *NOVO CONTATO PROFISSIONAL*

👤 *Nome:* ${data.name}
📧 *Email:* ${data.email}
${data.phone ? `📱 *Telefone:* ${data.phone}` : ''}
${data.company ? `🏢 *Empresa:* ${data.company}` : ''}

🎯 *Assunto:* ${this.getSubjectLabel(data.subject)}

💬 *Mensagem:*
${data.message}

${data.contactPreferences ? `📞 *Preferência de Contato:* ${data.contactPreferences.join(', ')}` : ''}

---
*Enviado via formulário profissional • ${new Date().toLocaleString('pt-BR')}*`;
    }
    
    // Agente 5 Backend: Formatar mensagem Email
    formatEmailMessage(data) {
        return {
            subject: `[CONTATO PROFISSIONAL] ${data.subject} - ${data.name}`,
            body: `NOVO CONTATO PROFISSIONAL

Nome: ${data.name}
Email: ${data.email}
${data.phone ? `Telefone: ${data.phone}` : ''}
${data.company ? `Empresa: ${data.company}` : ''}

Assunto: ${this.getSubjectLabel(data.subject)}

Mensagem:
${data.message}

${data.contactPreferences ? `Preferência de Contato: ${data.contactPreferences.join(', ')}` : ''}

---
Enviado via formulário profissional em ${new Date().toLocaleString('pt-BR')}`
        };
    }
    
    // Helper: Obter label do assunto
    getSubjectLabel(value) {
        const labels = {
            'oportunidade': 'Oportunidade de Carreira',
            'projeto': 'Proposta de Projeto',
            'consultoria': 'Consultoria em IA/Cybersecurity',
            'parceria': 'Parceria Estratégica',
            'palestra': 'Palestra/Mentoria',
            'outro': 'Outro'
        };
        return labels[value] || value;
    }
    
    // Agente 1 UX/UI: Estado de submit
    setSubmitting(submitting) {
        this.isSubmitting = submitting;
        
        if (submitting) {
            this.submitBtn.classList.add('btn-loading');
            this.submitBtn.disabled = true;
            this.submitBtn.innerHTML = '<span>Enviando...</span>';
        } else {
            this.submitBtn.classList.remove('btn-loading');
            this.submitBtn.disabled = false;
            this.submitBtn.innerHTML = '<span>📤</span><span>Enviar Mensagem</span>';
        }
    }
    
    // Agente 1 UX/UI: Limpar formulário
    clearForm() {
        if (!this.form) return;
        
        this.form.reset();
        
        // Limpar classes de validação
        this.form.querySelectorAll('.form-input, .form-textarea, .form-select').forEach(field => {
            field.classList.remove('success', 'error');
        });
        
        // Limpar mensagens de erro
        this.form.querySelectorAll('.form-error').forEach(error => {
            error.remove();
        });
        
        // Limpar upload de arquivo
        const fileText = document.getElementById('fileText');
        const fileUpload = document.getElementById('fileUpload');
        if (fileText && fileUpload) {
            fileText.textContent = 'Clique para anexar arquivo ou arraste aqui';
            fileUpload.classList.remove('has-file');
        }
        
        // Resetar contador de caracteres
        const charCount = document.getElementById('charCount');
        if (charCount) {
            charCount.textContent = '0 / 2000 caracteres';
            charCount.style.color = 'var(--text-muted)';
        }
        
        this.showToast('Formulário limpo com sucesso', 'info');
    }
    
    // Agente 4 Acessibilidade: Container de toast
    createToastContainer() {
        this.toastContainer = document.createElement('div');
        this.toastContainer.className = 'toast-container';
        document.body.appendChild(this.toastContainer);
    }
    
    // Agente 4 Acessibilidade: Sistema de notificações
    showToast(message, type = 'info', duration = 5000) {
        if (!this.toastContainer) {
            this.createToastContainer();
        }
        
        const toast = document.createElement('div');
        toast.className = `toast ${type}`;
        
        const icons = {
            success: '✅',
            error: '❌',
            warning: '⚠️',
            info: 'ℹ️'
        };
        
        toast.innerHTML = `
            <span style="font-size: 1.2rem;">${icons[type]}</span>
            <span>${message}</span>
        `;
        
        this.toastContainer.appendChild(toast);
        
        // Auto remover
        setTimeout(() => {
            toast.style.animation = 'slideInRight 0.3s ease-out reverse';
            setTimeout(() => {
                if (toast.parentNode) {
                    toast.parentNode.removeChild(toast);
                }
            }, 300);
        }, duration);
        
        // Agente 4 Acessibilidade: Anunciar para screen readers
        this.announceToScreenReader(message, type);
    }
    
    // Agente 4 Acessibilidade: Anúncio para screen readers
    announceToScreenReader(message, type) {
        const announcement = document.createElement('div');
        announcement.setAttribute('aria-live', 'polite');
        announcement.setAttribute('aria-atomic', 'true');
        announcement.className = 'sr-only';
        announcement.textContent = `${type}: ${message}`;
        document.body.appendChild(announcement);
        
        setTimeout(() => {
            if (announcement.parentNode) {
                announcement.parentNode.removeChild(announcement);
            }
        }, 1000);
    }
    
    // Agente 4 Acessibilidade: Mostrar termos (placeholder)
    showTerms() {
        this.showToast('Termos de privacidade: Seus dados serão usados apenas para contato profissional e não compartilhados com terceiros.', 'info', 8000);
    }
}

// Agente 4 Acessibilidade: CSS para screen readers
const style = document.createElement('style');
style.textContent = `
    .sr-only {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
    }
    
    .drag-over {
        border-color: var(--accent-cyan) !important;
        background: rgba(0, 242, 255, 0.05) !important;
    }
`;
document.head.appendChild(style);

// Inicializar quando DOM estiver pronto
document.addEventListener('DOMContentLoaded', () => {
    new ProfessionalContactForm();
});
