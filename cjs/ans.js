class ToggleAnswers {
    constructor() {
        // Store the toggle state
        this.answersHidden = false;
    }

    // Main function to toggle answer visibility
    toggle() {
        // Get all markdown preview views
        const markdownViews = document.querySelectorAll('.markdown-preview-view');
        
        // Find all answer sections (h4 elements with 'ans' text)
        markdownViews.forEach(view => {
            const answerHeaders = Array.from(view.querySelectorAll('h4')).filter(h => 
                h.textContent.toLowerCase().includes('ans')
            );
            
            // For each answer header, toggle the visibility of all elements until the next header
            answerHeaders.forEach(header => {
                let current = header.nextElementSibling;
                while (current && !current.matches('h1, h2, h3, h4, h5, h6')) {
                    // Toggle visibility
                    current.style.display = this.answersHidden ? 'block' : 'none';
                    header.style.display = this.answersHidden ? 'block' : 'none';
                    current = current.nextElementSibling;
                }
            });
        });
        
        // Toggle the state
        this.answersHidden = !this.answersHidden;
    }
}