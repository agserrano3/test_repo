// Controller for logger
function log(message, level = 'info') {
    console.log(`[${level.toUpperCase()}] ${new Date().toISOString()}: ${message}`);
}

module.exports = { log };
