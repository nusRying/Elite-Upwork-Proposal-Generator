// Upwork Scraper Logic
function scrapeJobData() {
    const jobTitle = document.querySelector('.job-title')?.innerText || '';
    const jobDescription = document.querySelector('.job-description')?.innerText || '';
    
    // Client History (Simplified for v1)
    const clientHistory = Array.from(document.querySelectorAll('.feedback-item'))
        .map(el => el.innerText)
        .join('\n');

    // Screening questions
    const questions = Array.from(document.querySelectorAll('.up-card-section h4'))
        .filter(el => el.innerText.toLowerCase().includes('you will cover'))
        .map(el => el.nextElementSibling?.innerText)
        .filter(Boolean);

    return {
        job_description: `${jobTitle}\n\n${jobDescription}`,
        client_history: clientHistory,
        screening_questions: questions
    };
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "scrape") {
        const data = scrapeJobData();
        sendResponse(data);
    }
});
